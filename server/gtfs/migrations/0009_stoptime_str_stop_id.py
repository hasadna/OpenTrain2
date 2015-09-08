# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0008_trip_str_service_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='stoptime',
            name='str_stop_id',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
