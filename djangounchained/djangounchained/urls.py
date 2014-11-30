from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView

def home(request): 
    return HttpResponse("<html><body><h2>Hello World</h2><a href='/simpletable'>\
        Link to a simple table</a></body></html>")
def simpletable(request):
    return HttpResponse("<html><body><table><tr><td>Row 1</td><td>blah</td></tr></body>\
        </html>")
    
urlpatterns = patterns('',
    # Examples:
   url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
   # url(r'^$', home),
   # url(r'^simpletable/$', simpletable),
)
