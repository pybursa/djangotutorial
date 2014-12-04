from django.conf.urls import patterns, url

from nine import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<question_id>\d+)/square/$', views.square, name='square'),
)
