# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0021_auto_20150908_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='arrival_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='departure_time',
            field=models.IntegerField(),
        ),
    ]
