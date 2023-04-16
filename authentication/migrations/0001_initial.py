# Generated by Django 4.0.5 on 2022-07-10 07:59
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.admin import User

def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com'
    superuser.set_password('admin')
    superuser.save()

class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
