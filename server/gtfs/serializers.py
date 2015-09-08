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
    class Meta:
        model = models.StopTime
        fields = (
            'arrival_time',
            'departure_time'
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

