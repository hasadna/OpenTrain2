from django.db import models
import csv
import os

import common.ot_utils

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
    agency_id = models.IntegerField(primary_key=True,default=1)
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
    agency = models.ForeignKey('Agency',null=True,blank=True)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_desc = models.TextField()
    route_type = models.IntegerField()
    route_color = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s : %s' % (self.route_id,self.route_long_name)

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
    filename = "calendar.txt"
    service_id = models.CharField(max_length=100,primary_key=True)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
        
    def set_start_date(self,value):
        self.start_date = common.ot_utils.parse_gtfs_date(value)
        
    def set_end_date(self,value):
        self.end_date = common.ot_utils.parse_gtfs_date(value)
        
    
    def __unicode__(self):
        return self.service_id

    
class Trip(GTFSModel):
    filename = "trips.txt"
    route = models.ForeignKey('Route')
    service = models.ForeignKey('Service',null=True)
    trip_id = models.CharField(max_length=100,primary_key=True)
    direction_id = models.IntegerField()
    shape_id = models.CharField(max_length=100)

    def __unicode__(self):
        return self.trip_id

    @classmethod
    def deser(cls, row):
        return Trip(route_id=row['route_id'],
                    direction_id=row['direction_id'],
                    shape_id=row['shape_id'])
            
class Stop(GTFSModel):
    filename = "stops.txt"
    stop_id = models.IntegerField(primary_key=True)
    stop_name = models.CharField(max_length=200)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    stop_url = models.URLField()
    location_type = models.IntegerField()
    
    def __unicode__(self):
        return self.stop_name

class StopTime(GTFSModel):
    filename = "stop_times.txt"
    trip = models.ForeignKey('Trip')
    arrival_time = models.IntegerField()
    departure_time = models.IntegerField()
    stop = models.ForeignKey('Stop')
    stop_sequence = models.IntegerField() 
    def set_arrival_time(self,value):
        self.arrival_time = common.ot_utils.normalize_time(value)
        
    def json_arrival_time(self):
        return common.ot_utils.denormalize_time_to_string(self.arrival_time) 
        
    def set_departure_time(self,value):
        self.departure_time = common.ot_utils.normalize_time(value)
    
    def json_departure_time(self):
        return common.ot_utils.denormalize_time_to_string(self.departure_time)
        
    def __unicode__(self):
        return '%s %s' % (self.arrival_time,self.stop.stop_name)
    
        
class Shape(GTFSModel):
    filename = "shapes.txt"
    shape_id = models.CharField(max_length=100,db_index=True)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.IntegerField()
    def __unicode__(self):
        return '%s : lon=%s lat=%s' % (self.shape_id,self.shape_pt_lat,self.shape_pt_lon) 
    
class ShapeJson(models.Model):
    shape_id = models.CharField(max_length=100,db_index=True)
    points = models.TextField()
    
    
    
