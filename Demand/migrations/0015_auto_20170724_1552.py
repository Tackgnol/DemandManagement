# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demand', '0014_auto_20170717_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Savings',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='Spend',
            field=models.FloatField(blank=True, default=0),
        ),
    ]