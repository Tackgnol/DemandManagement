# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demand', '0011_auto_20170711_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Activities',
            field=models.ManyToManyField(blank=True, related_name='activities', to='Demand.Activity'),
        ),
    ]