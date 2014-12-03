from django.shortcuts import render

def square(request):
    params = request.GET.dict()
    if not params['a']:
        params['error'] = 'Please pass a in request'
    if not params['b']:
        params['error'] = 'Please pass b in request'
    if not params['c']:
        params['error'] = 'Please pass c in request'
    return render(request, 'square.html', params)
