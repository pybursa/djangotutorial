from django.conf.urls import patterns, include, url
from nine.views import square, people, heroes_table, details

urlpatterns = patterns('',
     url(r'^square/$', square),
     url(r'^heroes/$', heroes_table),
     url(r'^heroes/(?P<hero>\w+)/$', details, name="details"),
)
