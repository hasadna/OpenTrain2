import django
from django.db import models
from django.utils import timezone


class Network(models.Model):
    bssid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    # we don't store the stop since it might change if we erase the GTFS data
    # stop id and stop code are not DB but from the GTFS - not sure what is the fixed one
    stop_id = models.CharField(max_length=5,default=0)
    stop_code = models.CharField(max_length=5,default=0)
    mod_time = models.DateTimeField('modification time', auto_now_add=True)

    def __unicode__(self):
        return ','.join([self.bssid, self.name])

    def get_stop_dict(self):
        from gtfs.models import Stop
        try:
            stop = Stop.objects.get(stop_id=self.stop_id)
            return {
                'id': stop.stop_id,
                'code': stop.stop_code,
                'name': stop.stop_name,
            }
        except Stop.DoesNotExist:
            return None

    def guess_stop(self):
        from gtfs.models import Stop
        if self.stop_id:
            return
        try:
            print('Guessed ok for {0}'.format(self.name))
            s = Stop.objects.get(stop_name=self.name)
            self.stop_id = s.stop_id
            self.stop_code = s.stop_code
            self.save()
        except Stop.DoesNotExist:
            return


class PositionReport(models.Model):
    network = models.ForeignKey(Network)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, default=0)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, default=0)
    report_time = models.DateTimeField('report time', default=django.utils.timezone.now)
    record_time = models.DateTimeField('record time')

    def __str__(self):
        return ','.join([str(self.record_time), str(self.latitude), str(self.longitude)])
