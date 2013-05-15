# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repository'
        db.create_table(u'codereader_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('origin_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('homepage_url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'codereader', ['Repository'])


    def backwards(self, orm):
        # Deleting model 'Repository'
        db.delete_table(u'codereader_repository')


    models = {
        u'codereader.repository': {
            'Meta': {'object_name': 'Repository'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'homepage_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'origin_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['codereader']