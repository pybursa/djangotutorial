from django.conf.urls import patterns, url

from nine import views

urlpatterns = patterns(
    '',
    url(r'^square$', views.square, name='square'),
)
