# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Engagement', '0011_auto_20170713_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmanagement',
            name='Completed',
            field=models.BooleanField(default=False),
        ),
    ]
