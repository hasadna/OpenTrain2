from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from . import models
from . import serializers
import gtfs.models


class NetworkViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Network.objects.all()
    serializer_class = serializers.NetworkSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.AddBssidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stop_id = serializer.validated_data['stop_id']
        if stop_id:
            stop_code = gtfs.models.Stop.objects.get(stop_id=stop_id)
        else:
            stop_code = 0
        serializer.save(stop_code=stop_code)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





