from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from datetime import date
import csv

from nine.models import Person

class IndexView(generic.ListView):
    template_name = 'nine/index.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return 'test'

def square(request):
    template_name = 'nine/square.html'
    try:
        a = int(request.GET.get('a'))
        b = int(request.GET.get('b'))
        c = int(request.GET.get('c'))
        result = str(a * b * c)
    except:
        result = 'Please input the values'
    return HttpResponse(result)

def heroes(request, name = None):

    try:
        csv_data = csv.reader(file('nine/data.csv'))
    except StandardError:
        raise StandardError("Can not read the file ")

    data = []
    for row in csv_data:
        data.append(row)
    data = data[1:]
    data_persons = []
    for row in data:
        current_person = Person(row[1], row[2], row[3], row[4])
        current_person
        data_persons.append(current_person)


    if name == None:
        result = 'Heroes list <br/>'
        result += 'id surname name birthdate nickname'
        for row in data:
            result += str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + ' <a href="' + str(row[4]).lower() + '/">' + str(row[4]) + '</a>'
            result += '\n <br/>'
    else:
        result = 'Hero: <br>'
        for row in data:
            if(row[4].lower() == name):
                result += str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + str(row[4])
        result += '<br/> List of heroes: ' + ' <a href="/nine/heroes/ "> Heroes </a>'
    return HttpResponse(result)

class Person:
    # Person initializer
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(int(birth_date[0:4]), int(birth_date[5:7]), int(birth_date[8:10]))

        if nickname is not None:
            self.nickname = nickname

    # Return age of person in str.
    def get_age(self):
        r = date.today() - self.birth_date
        print dir(r)
        return str(int(r.days / 365.25))

    # return fullname of person.
    def get_fullname(self):
        return self.surname + ' ' + self.first_name