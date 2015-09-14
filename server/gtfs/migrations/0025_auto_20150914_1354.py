# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0024_auto_20150913_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='str_stop_id',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='trip',
            name='str_service_id',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
