from django.shortcuts import render
from django.http import HttpResponse
from nine.models import Heroes, Square

# Create your views here.


def index(request):
    return HttpResponse("Hello world.")

def square(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    if (a == '') or (b == '') or (c == ''):
        return HttpResponse("Input parametres not correct.")
    else:
        result = Square(a, b, c)
        if result.solution == False:
            return HttpResponse("Have not solution in this case.")
        else:
            return render(request, 'nine/square.html', {'model': result})

def heroes(request):
    heros = Heroes('nine/data.csv')
    return render(request, 'nine/heroes.html', {'model': heros})


def heroes_details(request, nickname):
    heros = Heroes('nine/data.csv')
    hero = heros.get_hero(nickname)
    if nickname == 'None':
       return HttpResponse('hero not found')
    else:
        return render(request, 'nine/details.html', {'model': hero})    
