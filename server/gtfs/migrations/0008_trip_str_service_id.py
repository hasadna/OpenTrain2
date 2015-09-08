# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0007_auto_20150907_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='str_service_id',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
