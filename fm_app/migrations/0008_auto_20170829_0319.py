# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm_app', '0007_auto_20170825_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='flashNews',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='topNews',
            field=models.BooleanField(default=False),
        ),
    ]
