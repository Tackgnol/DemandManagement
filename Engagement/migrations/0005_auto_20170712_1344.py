# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Engagement', '0004_subproject_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='Complexity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Engagement.Complexity'),
        ),
    ]
