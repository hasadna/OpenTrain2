# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0015_auto_20150908_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shape',
            name='shape_pt_lat',
        ),
        migrations.RemoveField(
            model_name='shape',
            name='shape_pt_lon',
        ),
        migrations.RemoveField(
            model_name='shape',
            name='shape_pt_sequence',
        ),
    ]
