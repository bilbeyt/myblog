# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20150428_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='username',
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 21, 34, 58, 23357), verbose_name=b'Publish time'),
        ),
    ]
