# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0017_auto_20150908_1354'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShapeJson',
        ),
    ]
