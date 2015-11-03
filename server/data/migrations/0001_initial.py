# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('bssid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modification time')),
            ],
        ),
        migrations.CreateModel(
            name='PositionReport',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8, default=0)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8, default=0)),
                ('report_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='report time')),
                ('record_time', models.DateTimeField(verbose_name='record time')),
                ('network', models.ForeignKey(to='data.Network')),
            ],
        ),
    ]
