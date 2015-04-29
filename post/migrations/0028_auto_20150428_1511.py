# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20150428_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 15, 11, 11, 301558), verbose_name=b'Publish time'),
        ),
    ]
