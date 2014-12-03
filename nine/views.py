from django.shortcuts import render
from math import sqrt
from nine.models import Person
from csv import reader
from datetime import date, datetime

# Create your views here.
def square(request):
    mes = ''
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    c = request.GET.get('c', None)
    if a == '0':
        mes += "a is 0. "
    if a == '' or a is None:
       mes += 'a is not set. '
    if b == '' or b is None:
        mes += "b is not set. "
    if c == '' or c is None:
        mes += "c is not set. "
    if a != '' and a != '0' and a is not None and b !=''  and b is not None and c != '' and c is not None:
        a, b, c = int(a), int(b), int(c)
        d = b ** 2 - 4 * a * c
        if d < 0:
            mes = "there are no roots"
        elif d == 0:
            x = -b / 2 * a
            mes = str(x)
        elif d > 0:
            x1 = (-b + d ** (1/2.0)) / 2 * a
            x2 = (-b - d ** (1/2.0)) / (2 * a)
            mes = "The roots are " + str(round(x1, 2)) + " and " + str(round(x2, 2))


    return render(request, 'square.html', {'a' : mes})



def people(request):
    with open('data.csv', 'r') as data:
        people = list(reader(data))
        #Person.objects.all().delete()
        for row in people:
            if row[0] == "id":
                pass
            else:
                bd = row[3][0:4] + "/" + row[3][5:7] + "/" + row[3][8:10]
                bd = datetime.strptime(bd, "%Y/%m/%d")
                hero = Person(No = row[0], surname=row[1], name = row[2], birthdate=bd, nickname=row[4])
                hero.save()
    return render(request, 'people.html', {"people": Person.objects.all()})

def heroes_table(request):
    with open('data.csv', 'r') as data:
        heroes = list(reader(data))
    return render(request, 'heroes.html', {'head': heroes[0], 'heroes': heroes[1:]})

def details(request, hero=None):
    with open('data.csv', 'r') as data:
        heroes = list(reader(data))
        l= []
        for row in heroes[1:]:
            if row[4].lower() == hero.lower():
                l = row
                break
        if l is not None:
            return render(request, 'details.html', {'hero': l[1:]})