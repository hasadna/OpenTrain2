# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TtShape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtfs_shape_id', models.CharField(max_length=100, db_index=True)),
                ('gtfs_date_str', models.CharField(default=b'2014_dummy', max_length=20)),
                ('points', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TtStop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtfs_stop_id', models.IntegerField(null=True, db_index=True)),
                ('stop_name', models.CharField(max_length=200)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('stop_url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TtStopTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stop_sequence', models.IntegerField()),
                ('exp_arrival', models.DateTimeField()),
                ('exp_departure', models.DateTimeField()),
                ('stop', models.ForeignKey(to='timetable.TtStop')),
            ],
        ),
        migrations.CreateModel(
            name='TtTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtfs_trip_id', models.CharField(db_index=True, max_length=100, unique=True, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('from_stoptime', models.ForeignKey(related_name='first_stop', to='timetable.TtStopTime', null=True)),
                ('shape', models.ForeignKey(to='timetable.TtShape', null=True)),
                ('to_stoptime', models.ForeignKey(related_name='last_stop', to='timetable.TtStopTime', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ttstoptime',
            name='trip',
            field=models.ForeignKey(to='timetable.TtTrip'),
        ),
    ]
