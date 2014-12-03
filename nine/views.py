from django.shortcuts import render

def square(request):
    params = request.GET.dict()
    return render(request, 'square.html', params)
