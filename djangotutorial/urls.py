# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^tutorial/',
                           include('tutorial.urls', namespace="tutorial")),
                       url(r'^admin/', include(admin.site.urls)), )
