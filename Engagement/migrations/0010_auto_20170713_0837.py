# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Engagement', '0009_auto_20170712_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subproject',
            old_name='Parent',
            new_name='Project',
        ),
    ]
