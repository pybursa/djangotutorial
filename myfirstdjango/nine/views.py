from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def nine_square(request):
    r = render(request, 'square.html', {'testid': request.GET})
    return r


def nine_index(request):
    r = render(request, 'index.html')
    print type(r)
    return r

