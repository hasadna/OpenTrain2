# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0006_remove_trip_trip_headsign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='service',
            field=models.ForeignKey(to='gtfs.Service', null=True),
        ),
    ]
