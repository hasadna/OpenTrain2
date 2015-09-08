from django.utils import timezone
import datetime

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from . import models
from . import serializers
import common.ot_utils

class StopsViewSet(ReadOnlyModelViewSet):
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer


class TripsViewSet(GenericViewSet):
    serializer_class = serializers.TripSerializer
    queryset = models.Trip.objects.all()

    @list_route(url_path='date/today')
    def today(self, request):
        return self.trips_for_date(common.ot_utils.get_today())

    @list_route(url_path='date/(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)')
    def date(self, request,year,month,day):
        d = datetime.date(year=int(year),
                          month=int(month),
                          day=int(day))
        return self.trips_for_date(d)

    def trips_for_date(self,date):
        day_name_dict = dict()
        day_name_dict[date.strftime('%A').lower()] = True
        services = models.Service.objects.filter(start_date__lte=date,
                                                 end_date__gte=date)
        services = services.filter(**day_name_dict)

        today_trips = models.Trip.objects.filter(service__in=services).prefetch_related('stop_times')
        serializer = self.get_serializer(today_trips, many=True)
        return Response(serializer.data)