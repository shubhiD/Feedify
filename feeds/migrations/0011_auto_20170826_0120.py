# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 01:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20170826_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protoken',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 1, 20, 23, 248813, tzinfo=utc)),
        ),
    ]
