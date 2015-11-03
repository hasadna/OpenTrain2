from rest_framework import serializers, fields
from . import models


class NetworkSerializer(serializers.ModelSerializer):
    stop = serializers.DictField(source='get_stop_dict')
    class Meta:
        model = models.Network
        fields = ('bssid','stop')

class AddBssidSerializer(serializers.Serializer):
    stop_id = models.IntegerField(required=True)
    bssid = models.CharField(required=True)
    name = models.CharField(required=True)








