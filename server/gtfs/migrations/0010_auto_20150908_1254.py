# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0009_stoptime_str_stop_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptime',
            name='stop',
            field=models.ForeignKey(to='gtfs.Stop', null=True),
        ),
    ]
