# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-18 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Engagement', '0014_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]