# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0004_auto_20150907_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='route_text_color',
        ),
    ]
