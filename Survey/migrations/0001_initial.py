# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-07 10:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Engagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Demand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numeric', models.FloatField(blank=True, null=True)),
                ('Text', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bool', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InputType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=75)),
                ('Options', models.ManyToManyField(to='Survey.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=256)),
                ('AnswerRequired', models.BooleanField(default=False)),
                ('MultipleAnswers', models.BooleanField(default=False)),
                ('InputType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Survey.InputType')),
                ('OptionGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.OptionGroup')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('DefaultFor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Demand.Activity')),
                ('Questions', models.ManyToManyField(to='Survey.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Subheading', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Engagement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Engagement.SubProject')),
                ('QuestionSet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Survey.QuestionSet')),
                ('Respondent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='Section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Survey.Section'),
        ),
        migrations.AddField(
            model_name='question',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.Unit'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Options',
            field=models.ManyToManyField(blank=True, to='Survey.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Survey.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.Survey'),
        ),
    ]
