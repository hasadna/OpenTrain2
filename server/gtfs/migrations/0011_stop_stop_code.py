# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0010_auto_20150908_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='stop_code',
            field=models.IntegerField(null=True),
        ),
    ]
