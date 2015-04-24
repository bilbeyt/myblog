# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20150424_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 7, 23, 35, 945979), verbose_name=b'Publish time'),
        ),
    ]
