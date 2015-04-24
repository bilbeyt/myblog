# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_auto_20150424_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 15, 34, 51, 627162), verbose_name=b'Publish time'),
        ),
    ]
