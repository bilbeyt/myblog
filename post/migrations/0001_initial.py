# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 25, 8, 51, 58, 71532), verbose_name=b'Publish time')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
