from django.conf.urls import patterns, url

from nine import views

urlpatterns = patterns(
    '',
    url(r'^', views.square, name='square'),
    url(r'^square$', views.square, name='square'),
)
