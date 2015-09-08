from django.conf.urls import url, include
from rest_framework import routers
import gtfs.api

router = routers.SimpleRouter()
router.register('gtfs/stops',gtfs.api.StopsViewSet)
router.register('gtfs/trips',gtfs.api.TripsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
