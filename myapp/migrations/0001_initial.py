# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table('myapp_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Publisher'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('myapp', ['Book'])

        # Adding model 'Publisher'
        db.create_table('myapp_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('myapp', ['Publisher'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table('myapp_book')

        # Deleting model 'Publisher'
        db.delete_table('myapp_publisher')


    models = {
        'myapp.book': {
            'Meta': {'object_name': 'Book'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myapp.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'myapp.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myapp']