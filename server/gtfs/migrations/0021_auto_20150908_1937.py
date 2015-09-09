# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0020_auto_20150908_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='arrival_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='departure_time',
            field=models.TimeField(),
        ),
    ]
