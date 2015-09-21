from django.conf.urls import url, include
from rest_framework import routers
import gtfs.api
import data.api

router = routers.SimpleRouter()
router.register('gtfs/stops',gtfs.api.StopsViewSet)
router.register('gtfs/trips',gtfs.api.TripsViewSet)
router.register('gtfs/dates',gtfs.api.DatesViewSet,base_name='dates')
router.register('data/bssids',data.api.NetworkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]

