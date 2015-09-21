from rest_framework import serializers, fields
from . import models


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Network
        fields = ('id','bssid','name')



