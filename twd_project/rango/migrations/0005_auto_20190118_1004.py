# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-18 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20190117_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='view',
            new_name='views',
        ),
    ]