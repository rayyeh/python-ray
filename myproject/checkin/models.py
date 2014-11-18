from django.db import models
from django.contrib import admin

# Create your models here.
class Pan(models.Model):
    Checkin_choice = ((0, '未兌換'), (1, '已兌換'))
    pid = models.CharField("活動代號", max_length=4)
    pan = models.CharField("卡號", max_length=19)
    expiredate = models.CharField("有效期(yymm)", max_length=4)
    sid = models.CharField("歸戶號", max_length=10, null=False)
    checkin = models.IntegerField("兌換", choices=Checkin_choice)
    checkindate = models.DateTimeField("兌換交易日")

    def __unicode__(self):
        return self.pan

    class Meta(object):
        db_table = "pan"


class Prog(models.Model):
    Rule_choice = (('0', 'By Card'), ('1', 'By ID'))
    pid = models.CharField("活動代號", max_length=4, primary_key=True)
    startdate = models.DateField('啟用日')
    enddate = models.DateField('停用日')
    starttime = models.TimeField('啟用時間')
    endtime = models.TimeField('停用時間')
    rule = models.CharField("兌換辦法", max_length=1, choices=Rule_choice)
    memo = models.CharField("備註", max_length=50)

    def __unicode__(self):
        return self.pid + ';' + self.memo

    class Meta(object):
        db_table = "prog"


class Tid(models.Model):
    tid = models.CharField("端末機", max_length=8, primary_key=True)
    mid = models.CharField("特店代號", max_length=15)
    transeq = models.IntegerField("交易序號")
    pid = models.CharField("活動代號", max_length=4)

    def __unicode__(self):
        return self.tid + ';' + self.pid

    class Meta(object):
        db_table = "tid"


class Tranlog(models.Model):
    Reveflag_choice = (('0', '未沖正'), ('1', '已沖正'),)
    trandate = models.DateField("交易日")
    trantime = models.DateTimeField("交易時間", primary_key=True)
    tid = models.CharField("端末機", max_length=8)
    pan = models.CharField("卡號", max_length=19)
    pid = models.CharField("活動代號", max_length=4)
    resp = models.CharField("回應碼", max_length=2)
    authno = models.CharField("授權碼", max_length=6)
    traceno = models.CharField("交易序號", max_length=6)
    reveflag = models.CharField("是否沖正", max_length=1, choices=Reveflag_choice)

    def __unicode__(self):
        return self.pan + ';' + self.pid + ';' + self.resp


    class Meta(object):
        db_table = "tranlog"


class PanAdmin(admin.ModelAdmin):
    search_fields = ['^pan', '^sid']
    list_display = ('pid', 'pan', 'expiredate', 'sid', 'checkin', 'checkindate')
    list_display_links = ('pid', 'pan')
    # list_editable =['checkin']
    list_filter = ('pid', 'checkin')


class TidAdmin(admin.ModelAdmin):
    search_fields = ['^tid', '^pid']
    list_display = ('tid', 'mid', 'transeq', 'pid')


class ProgAdmin(admin.ModelAdmin):
    search_fields = ['^pid']
    list_display = ('pid', 'rule', 'startdate', 'starttime', 'enddate', 'endtime', 'memo')


class TranlogAdmin(admin.ModelAdmin):
    search_fields = ['^pan', '^tid', '^trandate', '^pid']
    list_display = ('trandate', 'trantime', 'tid', 'pan', 'pid', 'resp', 'authno', 'traceno', 'reveflag')
    readonly_fields = ('trandate', 'trantime', 'tid', 'pan', 'pid', 'resp', 'authno', 'traceno', 'reveflag')


admin.site.register(Pan, PanAdmin)
admin.site.register(Prog, ProgAdmin)
admin.site.register(Tid, TidAdmin)
admin.site.register(Tranlog, TranlogAdmin)
