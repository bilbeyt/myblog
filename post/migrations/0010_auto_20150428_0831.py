# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20150426_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 4, 28, 5, 31, 1, 413928, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 8, 30, 33, 903556), verbose_name=b'Publish time'),
        ),
    ]
