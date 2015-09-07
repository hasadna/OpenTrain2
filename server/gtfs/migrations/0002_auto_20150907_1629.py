# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
    ]
