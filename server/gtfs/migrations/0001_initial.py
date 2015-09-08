# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.IntegerField(default=1, max_length=255, serialize=False, primary_key=True)),
                ('agency_name', models.TextField()),
                ('agency_url', models.TextField()),
                ('agency_timezone', models.TextField()),
                ('agency_lang', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.IntegerField(serialize=False, primary_key=True)),
                ('route_short_name', models.CharField(max_length=255)),
                ('route_long_name', models.CharField(max_length=255)),
                ('route_desc', models.TextField()),
                ('route_type', models.IntegerField()),
                ('route_color', models.CharField(max_length=10)),
                ('route_text_color', models.CharField(max_length=20)),
                ('agency', models.ForeignKey(blank=True, to='gtfs.Agency', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shape_id', models.CharField(max_length=100, db_index=True)),
                ('shape_pt_lat', models.FloatField()),
                ('shape_pt_lon', models.FloatField()),
                ('shape_pt_sequence', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShapeJson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shape_id', models.CharField(max_length=100, db_index=True)),
                ('points', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.IntegerField(serialize=False, primary_key=True)),
                ('stop_name', models.CharField(max_length=200)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('stop_url', models.URLField()),
                ('location_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StopTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival_time', models.IntegerField()),
                ('departure_time', models.IntegerField()),
                ('stop_sequence', models.IntegerField()),
                ('stop', models.ForeignKey(to='gtfs.Stop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('direction_id', models.IntegerField()),
                ('shape_id', models.CharField(max_length=100)),
                ('wheelchair_accessible', models.IntegerField()),
                ('trip_headsign', models.CharField(max_length=100)),
                ('route', models.ForeignKey(to='gtfs.Route')),
                ('service', models.ForeignKey(to='gtfs.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(to='gtfs.Trip'),
        ),
    ]
