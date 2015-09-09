# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0022_auto_20150908_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='arrival_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='departure_time',
            field=models.CharField(max_length=20),
        ),
    ]
