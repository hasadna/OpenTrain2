# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0013_auto_20150908_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='shape_id',
            field=models.ForeignKey(to='gtfs.Shape', null=True),
        ),
    ]
