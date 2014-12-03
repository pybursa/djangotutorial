from django.conf.urls import patterns, include, url
from nine.views import nine_square,  nine_index


urlpatterns = patterns('',
    url(r'^$', nine_index),
    url(r'^square$', nine_square),
    url(r'^(?P<poll_id>\d+)/$', nine_square),
    url(r'^square/$', nine_square),

    #url(r'^(?P<course_slug>[\w-]+)/$', nine_view),
)
