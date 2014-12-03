from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from nine.views import square

urlpatterns = patterns('',
    url(r'^$', square),
    url(r'^nine/', include('nine.urls', namespace="nine")),
    url(r'^admin/', include(admin.site.urls)),
)
