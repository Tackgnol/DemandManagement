# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='User',
        ),
    ]
