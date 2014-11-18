# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting field 'Tranlog.datetime'
        db.delete_column('tranlog', 'datetime')

        # Changing field 'Tranlog.trantime'
        db.alter_column('tranlog', 'trantime', self.gf('django.db.models.fields.DateTimeField')(primary_key=True))

        # Adding unique constraint on 'Tranlog', fields ['trantime']
        db.create_unique('tranlog', ['trantime'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tranlog', fields ['trantime']
        db.delete_unique('tranlog', ['trantime'])

        # User chose to not deal with backwards NULL issues for 'Tranlog.datetime'
        raise RuntimeError("Cannot reverse this migration. 'Tranlog.datetime' and its values cannot be restored.")

        # Changing field 'Tranlog.trantime'
        db.alter_column('tranlog', 'trantime', self.gf('django.db.models.fields.TimeField')())


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
            'pan': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'resp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'reveflag': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'traceno': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'trandate': ('django.db.models.fields.DateField', [], {}),
            'trantime': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['checkin']
