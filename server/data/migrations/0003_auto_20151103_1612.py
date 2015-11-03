# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151103_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='stop_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='stop_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
