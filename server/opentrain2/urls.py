"""opentrain_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^data/', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/timetable/search-in/')),
    url(r'^timetable/', include('timetable.urls', namespace='timetable')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include('ot_api.urls', namespace='ot_api')),
    url(r'^static/jsi18n/he/django.js$', 'common.views.home'),
    # url(r'^privacy','common.views.privacy')
]
