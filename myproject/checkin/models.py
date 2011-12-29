from django.db import models
from django.contrib import admin

# Create your models here.
class Pan(models.Model):
  pid	   = models.CharField(max_length = 4)
  pan      = models.CharField(max_length = 19)
  expiredate = models.CharField(max_length = 4)
  sid	= models.CharField(max_length = 10,null=False)
  checkin = models.IntegerField()	
  checkindate = models.DateTimeField()

  def __unicode__(self):
    return self.pid+';'+self.pan
	
  class Meta(object):
    db_table = "pan"
	
class Prog(models.Model):
  pid	   = models.CharField(max_length = 4,primary_key=True)
  startdate  = models.DateField()
  enddate = models.DateField()
  starttime = models.TimeField()
  endtime = models.TimeField()
  rule = models.IntegerField()
  memo = models.CharField(max_length =50)  

  def __unicode__(self):
    return self.pid
  
  class Meta(object):
    db_table = "prog"
	
class Tid(models.Model):
  tid	   = models.CharField(max_length = 8,primary_key=True)
  mid = models.CharField(max_length =15)  
  transeq = models.IntegerField()
  pid = models.CharField(max_length = 4)

  def __unicode__(self):
    return self.tid
  
  class Meta(object):
    db_table = "tid"

class Tranlog(models.Model):
  trandate  = models.DateField()
  trantime  = models.TimeField()
  tid  = models.CharField(max_length = 8)
  pan      = models.CharField(max_length = 19)
  pid	   = models.CharField(max_length = 4)
  resp = models.CharField(max_length =2)
  authno = models.CharField(max_length =6)
  traceno = models.CharField(max_length =6)
  reveflag = models.CharField(max_length =1)
  
  class Meta(object):
    db_table = "tranlog"

	
class PanAdmin(admin.ModelAdmin):
  pass
	
class TidAdmin(admin.ModelAdmin):
  pass
	
class ProgAdmin(admin.ModelAdmin):
  pass
	
class TranlogAdmin(admin.ModelAdmin):
  pass

admin.site.register(Pan, PanAdmin)
admin.site.register(Prog, ProgAdmin)
admin.site.register(Tid, TidAdmin)
admin.site.register(Tranlog, TranlogAdmin)
