from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet


class StopsViewSet(ReadOnlyModelViewSet):
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer

