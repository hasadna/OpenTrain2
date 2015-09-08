# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0005_remove_route_route_text_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='trip_headsign',
        ),
    ]
