from django.db.models.expressions import RawSQL, F
from django.utils import timezone
import datetime

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ViewSet

from . import models
from . import serializers
import common.ot_utils


class ParamsParser:
    def parse_date_str(self, dt_str):
        d, m, y = dt_str.split('-')
        return datetime.date(year=int(y), month=int(m), day=int(d))

    def parse_time_str(self, time_str):
        h, m = time_str.split(':')
        return datetime.time(hour=int(h), minute=int(m))

    def combine_and_parse_date_time_str(self, dt_str, time_str):
        d = self.parse_date_str(dt_str)
        t = self.parse_time_str(time_str)
        return timezone.get_default_timezone.localize(datetime.datetime.combine(d, t))


class DatesViewSet(ViewSet):
    def list(self, request):
        start_date = models.Service.objects.earliest('start_date').start_date
        end_date = models.Service.objects.latest('end_date').end_date
        dates = []
        d = start_date
        while d <= end_date:
            dates.append({
                'date': d.isoformat(),
            })
            d += datetime.timedelta(days=1)
        ser = serializers.DateSerializer(dates, many=True)
        return Response(ser.data)


class StopsViewSet(ReadOnlyModelViewSet):
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer


class TripsViewSet(GenericViewSet, ParamsParser):
    serializer_class = serializers.TripSerializer
    queryset = models.Trip.objects.all()

    @list_route(url_path='date/today')
    def today(self, request):
        return self.trips_for_date(common.ot_utils.get_localtime_today())

    @list_route(url_path='date/(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)')
    def date(self, request, year, month, day):
        d = datetime.date(year=int(year),
                          month=int(month),
                          day=int(day))
        return self.trips_for_date(d)

    def trips_for_date(self, date):
        day_name_dict = dict()
        day_name_dict[date.strftime('%A').lower()] = True
        services = models.Service.objects.filter(start_date__lte=date,
                                                 end_date__gte=date)
        services = services.filter(**day_name_dict)

        date_trips = models.Trip.objects.filter(service__in=services).prefetch_related('stop_times')
        serializer = self.get_serializer(date_trips, many=True)
        return Response(serializer.data)

    @list_route(url_path='from-to')
    def fromto(self, request):
        from_stop = request.query_params.get('from_stop')
        to_stop = request.query_params.get('to_stop')
        date = self.parse_date_str(request.query_params.get('date'))
        time = self.parse_time_str(request.query_params.get('time'))
        time_in_seconds_since_0 = time.hour * 3600 + time.minute * 60
        min_time = max(time_in_seconds_since_0 - 600, 0)
        max_time = time_in_seconds_since_0 + 3600

        day_name_dict = dict()
        day_name_dict[date.strftime('%A').lower()] = True
        services = models.Service.objects.filter(start_date__lte=date,
                                                 end_date__gte=date)
        services = services.filter(**day_name_dict)

        trips = models.Trip.objects.filter(service__in=services)

        trips = trips.filter(stop_times__stop_id=from_stop)
        trips = trips.filter(stop_times__stop_id=to_stop)

        trips = trips.annotate(
            from_idx=RawSQL("select stop_sequence from gtfs_stoptime where stop_id=%s and trip_id=gtfs_trip.trip_id",
                            (from_stop,)))
        trips = trips.annotate(
            to_idx=RawSQL("select stop_sequence from gtfs_stoptime where stop_id=%s and trip_id=gtfs_trip.trip_id",
                          (to_stop,)))

        trips = trips.annotate(delta_idx=F('to_idx') - F('from_idx'))
        trips = trips.filter(delta_idx__gt=0)
        trips = trips.prefetch_related('stop_times')
        trips = [t for t in trips if min_time <= t.get_stop_time(int(from_stop)).departure_seconds_since_0 <= max_time]

        serializer = self.get_serializer(trips, many=True)
        return Response(serializer.data)
