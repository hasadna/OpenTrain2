from rest_framework import serializers, fields
from . import models


class StopSerializer(serializers.ModelSerializer):
    id = fields.IntegerField(source='stop_id')
    code = fields.IntegerField(source='stop_code')
    name = fields.CharField(source='stop_name')
    latlon = fields.ListField(source='get_latlon')

    class Meta:
        model = models.Stop
        fields = (
            'id',
            'code',
            'name',
            'latlon',
        )


class StopTimeSerializer(serializers.ModelSerializer):
    a = fields.CharField(source='arrival_time')
    d = fields.CharField(source='departure_time')
    s = fields.IntegerField(source='stop.stop_id')
    i = fields.IntegerField(source='stop_sequence')

    class Meta:
        model = models.StopTime
        fields = (
            'a',
            'd',
            's',
            'i'
        )


class TripSerializer(serializers.ModelSerializer):
    id = fields.CharField(source='trip_id')
    stop_times = StopTimeSerializer(many=True)

    class Meta:
        model = models.Trip
        fields = (
            'id',
            'stop_times'
        )

