# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0014_trip_shape_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shape',
            name='id',
        ),
        migrations.AlterField(
            model_name='shape',
            name='shape_id',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
