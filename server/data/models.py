import django
from django.db import models
from django.utils import timezone


class Network(models.Model):
    bssid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    mod_time = models.DateTimeField('modification time', default=django.utils.timezone.now)

    def __str__(self):
        return ','.join([str(self.bssid), str(self.name)])


class PositionReport(models.Model):
    network = models.ForeignKey(Network)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, default=0)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, default=0)
    report_time = models.DateTimeField('report time', default=django.utils.timezone.now)
    record_time = models.DateTimeField('record time')

    def __str__(self):
        return ','.join([str(self.record_time), str(self.latitude), str(self.longitude)])
