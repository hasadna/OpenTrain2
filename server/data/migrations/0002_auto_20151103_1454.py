# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='stop_code',
            field=models.CharField(max_length=5, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='stop_id',
            field=models.CharField(max_length=5, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='network',
            name='mod_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='modification time'),
        ),
    ]
