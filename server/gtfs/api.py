from django.utils import timezone

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models
from . import serializers

class StopsViewSet(ReadOnlyModelViewSet):
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer


class TripsViewSet(ReadOnlyModelViewSet):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    paginate_by = 100

    @list_route()
    def today(self, request):
        today = timezone.now().date()
        today_trips = models.Trip.objects.filter(service__start_date__lte=today,
                                                 service__end_data__gte=today)
        serializer = self.get_serializer(today_trips, many=True)
        return Response(serializer.data)