from rest_framework import serializers, fields
from . import models


class NetworkSerializer(serializers.ModelSerializer):
    stop = serializers.DictField(source='get_stop_dict')
    class Meta:
        model = models.Network
        fields = ('bssid','stop','name')


class AddBssidSerializer(serializers.Serializer):
    stop_id = serializers.IntegerField(required=True)
    bssid = serializers.CharField(required=True)
    name = serializers.CharField(required=True)








