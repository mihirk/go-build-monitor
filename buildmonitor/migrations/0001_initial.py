# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table(u'buildmonitor_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pipeline_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
        ))
        db.send_create_signal(u'buildmonitor', ['Configuration'])

        # Adding model 'BuildsToMonitor'
        db.create_table(u'buildmonitor_buildstomonitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('build', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('configuration', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buildmonitor.Configuration'])),
        ))
        db.send_create_signal(u'buildmonitor', ['BuildsToMonitor'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table(u'buildmonitor_configuration')

        # Deleting model 'BuildsToMonitor'
        db.delete_table(u'buildmonitor_buildstomonitor')


    models = {
        u'buildmonitor.buildstomonitor': {
            'Meta': {'object_name': 'BuildsToMonitor'},
            'build': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'configuration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buildmonitor.Configuration']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'buildmonitor.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'pipeline_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        }
    }

    complete_apps = ['buildmonitor']