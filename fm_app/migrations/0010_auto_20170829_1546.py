# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm_app', '0009_photoprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
