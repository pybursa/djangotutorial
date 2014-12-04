from django.conf.urls import patterns, url
from django.views.generic import RedirectView

# from nine import views

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(pattern_name='nine:quadratic-equation')),
    url(r'square/$', 'nine.views.quad_equation', name='quadratic-equation'),

)
