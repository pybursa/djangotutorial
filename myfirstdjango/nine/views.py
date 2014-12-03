from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def nine_square(request):
    if request.GET['a'] and request.GET['b'] and request.GET['c']:
        discr = int(request.GET['b'])**2 - 4 * int(request.GET['a']) * int(request.GET['c'])
        if discr > 0:
            import math
            x1 = (-int(request.GET['b']) + math.sqrt(discr)) / (2 * int(request.GET['a']))
            x2 = (-int(request.GET['b']) - math.sqrt(discr)) / (2 * int(request.GET['a']))
            r = render(request, 'square.html', {'x1': x1, 'x2': x2, 'testid': request.GET})
        elif discr == 0:
            x = -int(request.GET['b']) / (2 * (2 * int(request.GET['a'])))
            r = render(request, 'square.html', {'x': x, 'testid': request.GET})
        else:
            error = "No root"
            r = render(request, 'square.html', {'error': error, 'error': error})
        return r
    else:
        r = render(request, 'square.html', {'testid': request.GET})
        return r


def nine_index(request):
    r = render(request, 'index.html')
    print type(r)
    return r
