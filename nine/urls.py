from django.conf.urls import patterns, url

from nine import views

urlpatterns = patterns(
    '',
    url(r'^square/$', views.square, name='square'),
    url(r'^heroes/$', views.heroes, name='heroes'),
    url(r'^heroes/(?P<nickname>\w+)/$', views.detail, name='detail'),
)
