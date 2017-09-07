# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_remove_answer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=75)),
                ('Options', models.ManyToManyField(null=True, to='Survey.Option')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='OptionGroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.OptionGroup'),
        ),
    ]
