# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gtfs', '0018_delete_shapejson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='shape_id',
            new_name='shape',
        ),
    ]
