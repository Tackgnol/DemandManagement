# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0003_auto_20170802_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='Unit',
        ),
        migrations.AddField(
            model_name='question',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.Unit'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='Options',
            field=models.ManyToManyField(blank=True, to='Survey.Option'),
        ),
        migrations.AlterField(
            model_name='optiongroup',
            name='Options',
            field=models.ManyToManyField(to='Survey.Option'),
        ),
        migrations.AlterField(
            model_name='question',
            name='OptionGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.OptionGroup'),
        ),
    ]
