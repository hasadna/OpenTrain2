# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0003_remove_trip_wheelchair_accessible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='agency_lang',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='agency_timezone',
        ),
    ]
