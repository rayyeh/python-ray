import boto3
import datetime
from zoneinfo import ZoneInfo
from botocore.config import Config

# ----------- 設定 -----------
# 放入你的SNS TOPIC ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:your-aws-account-id:your-topic-name'
AWS_REGION = 'us-east-1'  # CloudFront metrics 都在 us-east-1 + Region=Global
TZ = ZoneInfo("Asia/Taipei")  # 台灣時間
# ---------------------------

CFG = Config(retries={'max_attempts': 5}, connect_timeout=2, read_timeout=10)

sns = boto3.client('sns', region_name=AWS_REGION, config=CFG)
cf = boto3.client('cloudfront', config=CFG)
cw = boto3.client('cloudwatch', region_name=AWS_REGION, config=CFG)


def month_window_taipei_to_utc():
    """
    以台北時間計算當月區間：
      [當月1日 00:00:00 Asia/Taipei, 目前時間 Asia/Taipei)
    並轉成 UTC 回傳 Start/End；同時回傳台北時間字串供信件顯示。
    """
    now_tpe = datetime.datetime.now(tz=TZ).replace(
        minute=0, second=0, microsecond=0)
    start_tpe = now_tpe.replace(day=1, hour=0)
    end_tpe = now_tpe  # 到目前為止

    # 轉成 UTC 給 CloudWatch
    start_utc = start_tpe.astimezone(datetime.timezone.utc)
    end_utc = end_tpe.astimezone(datetime.timezone.utc)

    # 標籤/顯示用（台北）
    label = start_tpe.strftime('%Y-%m')
    display_range = f"{start_tpe.strftime('%Y-%m-%d %H:%M:%S %Z')} ~ {end_tpe.strftime('%Y-%m-%d %H:%M:%S %Z')}"
    return start_utc, end_utc, label, display_range


def list_distributions():
    dists = []
    paginator = cf.get_paginator('list_distributions')
    for page in paginator.paginate():
        for d in page.get('DistributionList', {}).get('Items', []):
            dists.append({
                'Id': d['Id'],
                'Domain': d['DomainName'],
                'Comment': d.get('Comment', '')
            })
    return dists


def build_queries(dist_ids, metric, stat='Sum'):
    qs = []
    for i, did in enumerate(dist_ids):
        qs.append({
            'Id': f"q{i}",
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/CloudFront',
                    'MetricName': metric,
                    'Dimensions': [
                        {'Name': 'DistributionId', 'Value': did},
                        {'Name': 'Region', 'Value': 'Global'}
                    ]
                },
                'Period': 86400,   # 以日為粒度後加總
                'Stat': stat
            },
            'ReturnData': True
        })
    return qs


def fetch_metric_sum(dist_ids, start_utc, end_utc, metric):
    result = {did: 0 for did in dist_ids}
    for i in range(0, len(dist_ids), 100):  # 每批最多100條
        batch = dist_ids[i:i+100]
        out = cw.get_metric_data(
            MetricDataQueries=build_queries(batch, metric, 'Sum'),
            StartTime=start_utc,
            EndTime=end_utc,
            ScanBy='TimestampDescending'
        )
        mdr = out.get('MetricDataResults', [])
        for j, did in enumerate(batch):
            vals = mdr[j].get('Values', [])
            result[did] = int(sum(vals)) if vals else 0
    return result


def lambda_handler(event, context):
    start_utc, end_utc, label, display_range_tpe = month_window_taipei_to_utc()
    dists = list_distributions()

    if not dists:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"CloudFront 月報（台北時間）- {label}",
            Message="沒有找到任何 CloudFront distributions。"
        )
        return {"ok": True, "dists": 0}

    dist_ids = [d['Id'] for d in dists]

    # 抓取「當月（台北時間邊界）」Requests 與 BytesDownloaded
    req_sum = fetch_metric_sum(dist_ids, start_utc, end_utc, 'Requests')
    down_sum = fetch_metric_sum(
        dist_ids, start_utc, end_utc, 'BytesDownloaded')

    # 彙整
    rows = []
    total_req = 0
    total_bytes = 0
    for d in dists:
        did = d['Id']
        r = req_sum.get(did, 0)
        b = down_sum.get(did, 0)
        rows.append({
            'id': did,
            'domain': d['Domain'],
            'requests': r,
            'gb_down': b / (1024 ** 3)
        })
        total_req += r
        total_bytes += b

    # 依下載量排序
    rows.sort(key=lambda x: x['gb_down'], reverse=True)

    # 信件內容（雙換行讓SNS郵件排版穩定）
    lines = []
    lines.append("🌍 CloudFront 當月用量報表（台北時間）")
    lines.append(f"月份：{label}")
    lines.append(f"區間（台北時間）：{display_range_tpe}")
    lines.append(f"Distributions：{len(rows)}")
    lines.append(f"總 Requests：{total_req:,}")
    lines.append(f"總下載量：{total_bytes/(1024**3):,.2f} GB")
    lines.append("")

    for r in rows:
        lines.append(f"{r['domain']} ({r['id']})")
        lines.append(f"  Requests : {r['requests']:,}")
        lines.append(f"  Download : {r['gb_down']:,.2f} GB")
        lines.append("")

    msg = "```\n" + "\n".join(lines) + "\n```"

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"CloudFront 當月用量報表（台北時間）- {label}",
        Message=msg
    )

    return {
        "ok": True,
        "dists": len(rows),
        "start_utc": start_utc.isoformat(),
        "end_utc": end_utc.isoformat(),
        "tz": "Asia/Taipei"
    }
