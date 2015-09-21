from rest_framework.viewsets import mixins, GenericViewSet

from . import models
from . import serializers


class NetworkViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Network.objects.all()
    serializer_class = serializers.NetworkSerializer


