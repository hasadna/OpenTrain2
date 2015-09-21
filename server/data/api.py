from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ViewSet

from . import models
from . import serializers


class NetworkViewSet(ReadOnlyModelViewSet):
    queryset = models.Network.objects.all()
    serializer_class = serializers.NetworkSerializer


