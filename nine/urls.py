from django.conf.urls import patterns, url

from nine import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^square', views.square, name='square'),
    url(r'^heroes/(?P<nickname>[\w-]+)$', views.heroes_details, name='heroes_details'),
    url(r'^heroes', views.heroes, name='heroes'),
)
