# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fm_app', '0011_auto_20170830_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosmodel',
            name='poster',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='video_gallery/poster'),
            preserve_default=False,
        ),
    ]
