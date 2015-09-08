import time
import logging
import os
from collections import defaultdict

from django.conf import settings
from django.apps import apps
from django.db.models import F

from . import models

LOGGER = logging.getLogger(__name__)


class Importer(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def read_txt(self, filename, cond):
        full_path = os.path.join(self.dirname, filename)
        result = []
        t1 = time.time()
        with open(full_path) as fh:
            header = fh.readline().strip().split(',')
            len_header = len(header)
            for idx, row in enumerate(fh):
                values = row.strip().split(',')
                assert len_header == len(values)
                rowdict = dict()
                i = 0
                for v in values:
                    rowdict[header[i]] = v
                    i += 1
                if cond(rowdict):
                    result.append(rowdict)
                if (2 + idx) % 1000000 == 0:
                    LOGGER.debug('%s: %s rows processed so far', filename, idx + 2)
            t2 = time.time()
            LOGGER.debug('%s: returning %s from %s rows, in %.2f seconds', filename, len(result), idx + 1, t2 - t1)
        return result

    def import_all(self):
        LOGGER.info('DEBUG = %s', settings.DEBUG)
        self.import_agency()
        self.import_routes()
        self.import_trips()
        self.import_services()
        self.import_stop_times()
        self.import_stops()
        self.import_shapes()
        models = apps.get_app_config('gtfs').models.values()
        for model in models:
            LOGGER.info('model %s: %s', model.__name__, model.objects.count())

    def import_agency(self):
        LOGGER.info('importing agency')
        agencies = self.read_txt('agency.txt', cond=lambda a: 'rail' in a['agency_url'])
        assert len(agencies) == 1
        a = models.Agency.from_row(agencies[0])
        self.agency_id = a.agency_id

    def import_routes(self):
        LOGGER.info('importing routes')
        routes = self.read_txt('routes.txt', cond=lambda x: x['agency_id'] == self.agency_id)
        models.Route.from_rows(routes)

    def import_trips(self):
        LOGGER.info('importing trips')
        route_ids = set(models.Route.objects.values_list('route_id', flat=True))
        trips = self.read_txt('trips.txt', cond=lambda x: int(x['route_id']) in route_ids)
        models.Trip.from_rows(trips)

    def import_services(self):
        LOGGER.info('importing services')
        services_ids = set(models.Trip.objects.values_list('str_service_id', flat=True))
        services = self.read_txt('calendar.txt', cond=lambda x: x['service_id'] in services_ids)
        assert len(services) == len(services_ids)
        models.Service.from_rows(services)
        # now reupdate the trips
        models.Trip.objects.all().update(service_id=F('str_service_id'))
        assert models.Trip.objects.filter(service__isnull=True).count() == 0

    def import_stop_times(self):
        LOGGER.info('importing stop times')
        trip_ids = set(models.Trip.objects.values_list('trip_id', flat=True))
        stop_times = self.read_txt('stop_times.txt', cond=lambda x: x['trip_id'] in trip_ids)
        models.StopTime.from_rows(stop_times)

    def import_stops(self):
        LOGGER.info('importing stops')
        stop_ids = set(models.StopTime.objects.values_list('str_stop_id', flat=True).distinct())
        stops = self.read_txt('stops.txt', cond=lambda x: x['stop_id'] in stop_ids)
        assert len(stop_ids) == len(stops)
        models.Stop.from_rows(stops)
        # now reupdate the stop times
        models.StopTime.objects.all().update(stop_id=F('str_stop_id'))
        assert models.StopTime.objects.filter(stop__isnull=True).count() == 0

    def import_shapes(self):
        LOGGER.info('importing shapes')
        shape_ids = set(models.Trip.objects.values_list('str_shape_id', flat=True))
        assert len(shape_ids) > 10
        shape_points = self.read_txt('shapes.txt', cond=lambda x: x['shape_id'] in shape_ids)
        points_for_shape = defaultdict(list)
        for p in shape_points:
            points_for_shape[p['shape_id']].append(p)
        rows = []
        for shape_id, points in points_for_shape.iteritems():
            rows.append({
                'shape_id': shape_id,
                'points': [[float(p['shape_pt_lat']), float(p['shape_pt_lon'])] for p in
                           sorted(points, key=lambda x: int(x['shape_pt_sequence']))]
            })
        models.Shape.from_rows(rows)
        models.Trip.objects.all().update(shape_id=F('str_shape_id'))
        assert models.Trip.objects.filter(shape__isnull=True).count() == 0
