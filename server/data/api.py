from rest_framework import status, exceptions
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from . import models
from . import serializers
import gtfs.models


class NetworkViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Network.objects.all()
    serializer_class = serializers.NetworkSerializer

    @list_route(methods=['POST'])
    def add(self, request, *args, **kwargs):
        serializer = serializers.AddBssidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stop_id = serializer.validated_data['stop_id']
        if stop_id:
            try:
                stop = gtfs.models.Stop.objects.get(stop_id=stop_id)
            except gtfs.models.Stop.DoesNotExist:
                raise exceptions.ValidationError({'stop_id': 'Illegal stop id'})

        n = models.Network.objects.create(stop_code=stop.stop_code if stop else 0,
                                          stop_id=stop_id,
                                          name=serializer.validated_data['name'],
                                          bssid=serializer.validated_data['bssid'])

        s = self.get_serializer(n)

        return Response(s.data, status=status.HTTP_201_CREATED)




