# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0002_auto_20150907_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='wheelchair_accessible',
        ),
    ]
