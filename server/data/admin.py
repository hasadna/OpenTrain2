from django.contrib import admin

# Register your models here.
from .models import Network, PositionReport


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('bssid', 'name', 'stop_id', 'stop_code', 'mod_time')


class PositionReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['network', 'record_time']}),
        ('Location', {'fields': ['latitude', 'longitude']})  # 'classes': ['collapse']
    ]
    list_display = ('network', 'record_time', 'latitude', 'longitude')


admin.site.register(Network, NetworkAdmin)
admin.site.register(PositionReport, PositionReportAdmin)
