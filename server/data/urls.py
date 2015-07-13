from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit$', views.submit_network, name='addNetwork'),
    url(r'^ls$', views.network_list, name='networkList')
]
