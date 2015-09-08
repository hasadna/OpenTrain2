# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0016_auto_20150908_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shapejson',
            name='points',
        ),
        migrations.AddField(
            model_name='shape',
            name='points',
            field=models.TextField(null=True),
        ),
    ]
