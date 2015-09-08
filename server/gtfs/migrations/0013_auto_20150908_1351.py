# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0012_remove_stop_stop_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='shape_id',
            new_name='str_shape_id',
        ),
    ]
