# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0016_auto_20170826_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=100)),
                ('oauth_secret', models.CharField(max_length=100)),
                ('oauth_token', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=100)),
                ('since_id', models.IntegerField()),
                ('json_data', models.TextField()),
            ],
            options={
                'ordering': ['-since_id'],
                'verbose_name_plural': 'UserTweet',
            },
        ),
        migrations.DeleteModel(
            name='ProToken',
        ),
        migrations.DeleteModel(
            name='Tweets',
        ),
    ]
