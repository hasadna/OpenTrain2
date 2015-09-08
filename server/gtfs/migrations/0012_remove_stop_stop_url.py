# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0011_stop_stop_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stop',
            name='stop_url',
        ),
    ]
