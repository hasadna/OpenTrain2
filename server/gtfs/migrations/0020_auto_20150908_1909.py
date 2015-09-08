# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0019_auto_20150908_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(related_name='stop_times', to='gtfs.Trip'),
        ),
    ]
