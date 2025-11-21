import boto3
import datetime
from botocore.config import Config

CFG = Config(retries={'max_attempts': 5}, connect_timeout=2, read_timeout=8)

sns = boto3.client('sns', region_name='us-east-1', config=CFG)   # SNS 放你想用的區
s3 = boto3.client('s3', config=CFG)

TOPIC_ARN = 'arn:aws:sns:us-east-1:your-aws-account-id:your-topic-name'  # 換成你的SNS TOPIC ARN

# 快取：不同區域的 CloudWatch client
cw_clients = {}


def cloudwatch_in(region: str):
    if region not in cw_clients:
        cw_clients[region] = boto3.client(
            'cloudwatch', region_name=region, config=CFG)
    return cw_clients[region]


def get_bucket_region(bucket: str) -> str:
    # get_bucket_location 回 None 代表 us-east-1
    r = s3.get_bucket_location(Bucket=bucket).get('LocationConstraint')
    return r or 'us-east-1'


def list_storage_types_for_bucket(cw, bucket: str):
    """在正確區域的 CloudWatch 列出該 bucket 的 StorageType 清單"""
    paginator = cw.get_paginator('list_metrics')
    types = set()
    for page in paginator.paginate(
        Namespace='AWS/S3',
        MetricName='BucketSizeBytes',
        Dimensions=[{'Name': 'BucketName', 'Value': bucket}]
    ):
        for m in page.get('Metrics', []):
            for d in m.get('Dimensions', []):
                if d['Name'] == 'StorageType':
                    types.add(d['Value'])
    return sorted(types)


def get_latest_bytes(cw, bucket: str, storage_type: str):
    """到正確區域抓該 StorageType 最新一天的 BucketSizeBytes（bytes）"""
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(days=3)  # S3 儲存量每日更新，回溯幾天避免延遲
    resp = cw.get_metric_statistics(
        Namespace='AWS/S3',
        MetricName='BucketSizeBytes',
        Dimensions=[
            {'Name': 'BucketName',  'Value': bucket},
            {'Name': 'StorageType', 'Value': storage_type}
        ],
        StartTime=start, EndTime=end, Period=86400, Statistics=['Average']
    )
    dps = sorted(resp.get('Datapoints', []), key=lambda x: x['Timestamp'])
    return dps[-1]['Average'] if dps else None  # bytes


def get_bucket_size_kb_total(bucket: str, region: str):
    cw = cloudwatch_in(region)
    stypes = list_storage_types_for_bucket(cw, bucket)
    if not stypes:
        return None  # 多半是空 bucket 或指標尚未產生
    total = 0
    has_data = False
    for st in stypes:
        val = get_latest_bytes(cw, bucket, st)
        if val is not None:
            total += val
            has_data = True
    return (total / 1024.0) if has_data else None  # KB


def lambda_handler(event, context):
    buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
    rows = []
    for b in buckets:
        region = get_bucket_region(b)
        kb = get_bucket_size_kb_total(b, region)
        rows.append((b, region, kb))

    # 依用量排序（N/A 放最後）
    rows.sort(key=lambda x: (-1 if x[2] is None else x[2]), reverse=True)

    # 明確逐行列印，每個 bucket 獨立一行
    report_lines = []
    report_lines.append("📦 S3 Storage Report (All buckets, KB)")
    report_lines.append(f"Total buckets: {len(rows)}")
    report_lines.append("")  # 空行
    for b, region, kb in rows:
        report_lines.append(
            f"{b} [{region}]: {'N/A' if kb is None else f'{kb:,.2f} KB'}")

    # 以 \n 連接，確保每行分開
    msg = "```\n" + "\n\n".join(report_lines) + "\n```"

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='S3 Monthly Usage Report (KB)',
        Message=msg
    )

    return {"buckets": len(buckets)}
