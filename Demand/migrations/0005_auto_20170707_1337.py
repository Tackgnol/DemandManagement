# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demand', '0004_auto_20170707_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttocategory',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='projecttocategory',
            name='Project',
        ),
        migrations.AddField(
            model_name='category',
            name='Projects',
            field=models.ManyToManyField(blank=True, to='Demand.Project'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='Projects',
            field=models.ManyToManyField(blank=True, to='Demand.Project'),
        ),
        migrations.AlterField(
            model_name='country',
            name='Projects',
            field=models.ManyToManyField(blank=True, to='Demand.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Actions',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='Comments',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='LastUpadate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Savings',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Spend',
            field=models.FloatField(blank=True),
        ),
        migrations.DeleteModel(
            name='ProjectToCategory',
        ),
    ]
