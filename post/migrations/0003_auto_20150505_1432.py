# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_deneme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deneme',
        ),
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
