# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pan'
        db.create_table('pan', (
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True)),
            ('pan', self.gf('django.db.models.fields.CharField')(max_length=19, primary_key=True)),
            ('expiredate', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('checkin', self.gf('django.db.models.fields.IntegerField')()),
            ('checkindate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('checkin', ['Pan'])

        # Adding model 'Prog'
        db.create_table('prog', (
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True)),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('enddate', self.gf('django.db.models.fields.DateTimeField')()),
            ('starttime', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('endtime', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rule', self.gf('django.db.models.fields.IntegerField')()),
            ('memo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('checkin', ['Prog'])

        # Adding model 'Tid'
        db.create_table('tid', (
            ('tid', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('mid', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('transeq', self.gf('django.db.models.fields.IntegerField')()),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('checkin', ['Tid'])

        # Adding model 'Tranlog'
        db.create_table('tranlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trandate', self.gf('django.db.models.fields.DateTimeField')()),
            ('trantime', self.gf('django.db.models.fields.DateTimeField')()),
            ('tid', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('pan', self.gf('django.db.models.fields.CharField')(max_length=19)),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('resp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('authno', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('traceno', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('reveflag', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('checkin', ['Tranlog'])


    def backwards(self, orm):
        
        # Deleting model 'Pan'
        db.delete_table('pan')

        # Deleting model 'Prog'
        db.delete_table('prog')

        # Deleting model 'Tid'
        db.delete_table('tid')

        # Deleting model 'Tranlog'
        db.delete_table('tranlog')


    models = {
        'checkin.pan': {
            'Meta': {'object_name': 'Pan', 'db_table': "'pan'"},
            'checkin': ('django.db.models.fields.IntegerField', [], {}),
            'checkindate': ('django.db.models.fields.DateTimeField', [], {}),
            'expiredate': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pan': ('django.db.models.fields.CharField', [], {'max_length': '19', 'primary_key': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'})
        },
        'checkin.prog': {
            'Meta': {'object_name': 'Prog', 'db_table': "'prog'"},
            'enddate': ('django.db.models.fields.DateTimeField', [], {}),
            'endtime': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'rule': ('django.db.models.fields.IntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {}),
            'starttime': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'resp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'reveflag': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'traceno': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'trandate': ('django.db.models.fields.DateTimeField', [], {}),
            'trantime': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['checkin']
