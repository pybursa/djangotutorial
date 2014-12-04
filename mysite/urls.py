from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nine/square$', 'nine.views.square'),
    url(r'^nine/heroes/$', 'nine.views.heroes'),
    url(r'^nine/heroes/(?P<name>\w{0,50})/$', 'nine.views.heroes'),
)
