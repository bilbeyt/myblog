# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20150428_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 12, 32, 19, 468004), verbose_name=b'Publish time'),
        ),
    ]
