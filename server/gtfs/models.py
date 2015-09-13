from django.db import models
import json
import common.ot_utils
import datetime


class GTFSModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def from_rows(cls, rows):
        objects = [cls.deser(row) for row in rows]
        cls.objects.bulk_create(objects)

    @classmethod
    def from_row(cls, row):
        result = cls.deser(row)
        result.save()
        return result


class Agency(GTFSModel):
    agency_id = models.IntegerField(primary_key=True, default=1)
    agency_name = models.TextField()
    agency_url = models.TextField()

    def __unicode__(self):
        return self.agency_name

    @classmethod
    def deser(cls, row):
        return Agency(agency_id=row['agency_id'],
                      agency_name=row['agency_name'],
                      agency_url=row['agency_url'])


class Route(GTFSModel):
    route_id = models.IntegerField(primary_key=True)
    agency = models.ForeignKey('Agency', null=True, blank=True)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_desc = models.TextField()
    route_type = models.IntegerField()
    route_color = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s : %s' % (self.route_id, self.route_long_name)

    @classmethod
    def deser(cls, row):
        return Route(agency_id=row['agency_id'],
                     route_id=row['route_id'],
                     route_short_name=row['route_short_name'],
                     route_long_name=row['route_long_name'],
                     route_desc=row['route_desc'],
                     route_type=row['route_type'],
                     route_color=row['route_color'],
                     )


class Service(GTFSModel):
    service_id = models.CharField(max_length=100, primary_key=True)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    @classmethod
    def deser(cls, row):
        result = Service(service_id=row['service_id'])
        for f in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            setattr(result, f, common.ot_utils.parse_bool(row[f]))
        result.start_date = common.ot_utils.parse_gtfs_date(row['start_date'])
        result.end_date = common.ot_utils.parse_gtfs_date(row['end_date'])
        return result

    def __unicode__(self):
        return self.service_id


class Trip(GTFSModel):
    filename = "trips.txt"
    route = models.ForeignKey('Route')
    service = models.ForeignKey('Service', null=True)
    str_service_id = models.CharField(max_length=50, default='')
    trip_id = models.CharField(max_length=100, primary_key=True)
    direction_id = models.IntegerField()
    str_shape_id = models.CharField(max_length=100)
    shape = models.ForeignKey('Shape', null=True)

    def get_stop_time(self, stop_id):
        for stop_time in self.stop_times.all():
            if stop_time.stop_id == stop_id:
                return stop_time
        raise Exception('Cannot find stop_time with stop_id = {0}'.format(stop_id))

    def __unicode__(self):
        return self.trip_id

    @classmethod
    def deser(cls, row):
        return Trip(trip_id=row['trip_id'],
                    route_id=row['route_id'],
                    direction_id=row['direction_id'],
                    str_shape_id=row['shape_id'],
                    str_service_id=row['service_id'])


class Stop(GTFSModel):
    filename = "stops.txt"
    stop_id = models.IntegerField(primary_key=True)
    stop_code = models.IntegerField(null=True)
    stop_name = models.CharField(max_length=200)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    location_type = models.IntegerField()

    def get_latlon(self):
        return [self.stop_lat, self.stop_lon]

    @classmethod
    def deser(cls, row):
        result = Stop()
        result.stop_id = row['stop_id']
        result.stop_code = row['stop_code']
        result.stop_name = row['stop_name']
        result.stop_lat = row['stop_lat']
        result.stop_lon = row['stop_lon']
        result.location_type = row['location_type']
        return result

    def __unicode__(self):
        return self.stop_name


class StopTime(GTFSModel):
    filename = "stop_times.txt"
    trip = models.ForeignKey('Trip',related_name='stop_times')
    arrival_time = models.CharField(max_length=20)
    arrival_seconds_since_0 = models.IntegerField(null=True)
    departure_time = models.CharField(max_length=20)
    departure_seconds_since_0 = models.IntegerField(null=True)
    stop = models.ForeignKey('Stop', null=True)
    stop_sequence = models.IntegerField()
    str_stop_id = models.CharField(max_length=20, default='')

    @classmethod
    def time_string_to_seconds(cls, time_str):
        h,m,s=(int(x) for x in time_str.split(':'))
        return h*3600 + m*60 + s

    @classmethod
    def deser(cls, row):
        result = StopTime()
        result.trip_id = row['trip_id']
        result.arrival_time = row['arrival_time']
        result.departure_time = row['departure_time']
        result.arrival_seconds_since_0 = cls.time_string_to_seconds(result.arrival_time)
        result.departure_seconds_since_0 = cls.time_string_to_seconds(result.departure_time)
        result.stop_sequence = int(row['stop_sequence'])
        result.str_stop_id = row['stop_id']
        return result

    def __unicode__(self):
        return '%s %s' % (self.arrival_time, self.stop.stop_name)


class Shape(GTFSModel):
    shape_id = models.CharField(max_length=100, primary_key=True)
    points = models.TextField(null=True)  # json

    @classmethod
    def deser(cls, row):
        return Shape(shape_id=row['shape_id'],
                     points=json.dumps(row['points']))
