from django.conf.urls import patterns, url

from tutorial import views

urlpatterns = patterns('',
                       url(r'^$', views.Index.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.Detail.as_view(),
                           name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.Results.as_view(),
                           name='results'),
                       url(r'^(?P<pk>\d+)/vote/$', views.Vote.as_view(),
                           name='vote'),
)