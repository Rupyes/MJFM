# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fm_app', '0017_auto_20170902_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_day', models.CharField(choices=[('su', 'Sunday'), ('mo', 'Monday'), ('tu', 'Tuesday'), ('we', 'Wednesday'), ('th', 'Thursday'), ('fr', 'Friday'), ('sa', 'Saturday')], default='su', max_length=10)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fm_app.Day')),
            ],
        ),
    ]
