# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0023_auto_20150908_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='stoptime',
            name='arrival_seconds_since_0',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stoptime',
            name='departure_seconds_since_0',
            field=models.IntegerField(null=True),
        ),
    ]
