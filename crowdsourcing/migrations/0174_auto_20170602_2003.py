# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 20:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0173_auto_20170601_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='timeout',
            field=models.DurationField(default=datetime.timedelta(0, 28800), null=True),
        ),
    ]
