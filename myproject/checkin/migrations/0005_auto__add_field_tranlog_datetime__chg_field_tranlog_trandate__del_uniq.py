# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Tranlog', fields ['trandate']
        db.delete_unique('tranlog', ['trandate'])

        # Adding field 'Tranlog.datetime'
        db.add_column('tranlog', 'datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 12, 30), primary_key=True), keep_default=False)

        # Changing field 'Tranlog.trandate'
        db.alter_column('tranlog', 'trandate', self.gf('django.db.models.fields.DateField')())


    def backwards(self, orm):
        
        # Deleting field 'Tranlog.datetime'
        db.delete_column('tranlog', 'datetime')

        # Changing field 'Tranlog.trandate'
        db.alter_column('tranlog', 'trandate', self.gf('django.db.models.fields.DateField')(primary_key=True))

        # Adding unique constraint on 'Tranlog', fields ['trandate']
        db.create_unique('tranlog', ['trandate'])


    models = {
        'checkin.pan': {
            'Meta': {'object_name': 'Pan', 'db_table': "'pan'"},
            'checkin': ('django.db.models.fields.IntegerField', [], {}),
            'checkindate': ('django.db.models.fields.DateTimeField', [], {}),
            'expiredate': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'checkin.prog': {
            'Meta': {'object_name': 'Prog', 'db_table': "'prog'"},
            'enddate': ('django.db.models.fields.DateField', [], {}),
            'endtime': ('django.db.models.fields.TimeField', [], {}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'rule': ('django.db.models.fields.IntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'starttime': ('django.db.models.fields.TimeField', [], {})
        },
        'checkin.tid': {
            'Meta': {'object_name': 'Tid', 'db_table': "'tid'"},
            'mid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'transeq': ('django.db.models.fields.IntegerField', [], {})
        },
        'checkin.tranlog': {
            'Meta': {'object_name': 'Tranlog', 'db_table': "'tranlog'"},
            'authno': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'resp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'reveflag': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'traceno': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'trandate': ('django.db.models.fields.DateField', [], {}),
            'trantime': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['checkin']
