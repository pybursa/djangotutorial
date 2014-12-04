import csv
from datetime import datetime, date

from django.http import HttpResponse
from django.shortcuts import render


def get_discr(a, b, c):
    d = b**2 - 4*a*c
    return d


def get_eq_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x


def quad_equation(request):
    args_warning = "You must provide all three coefficients equation!"
    result_message = "Roots of the equation do not exist"
    arguments = ['a', 'b', 'c']
    context_dict = {}
    for arg in arguments:
        value = request.GET.get(arg)
        if value is not None:
            value = int(value)
            context_dict[arg] = value
        else:
            return HttpResponse(args_warning)

    a = context_dict['a']
    b = context_dict['b']
    c = context_dict['c']
    d = get_discr(a, b, c)
    if d < 0:
        return HttpResponse(result_message)
    else:
        x1 = get_eq_root(a, b, d)
        x2 = get_eq_root(a, b, d, order=2)
        if x1 == x2:
            result_message = "There is one root: x1 = x2 = %g" % x1
        else:
            result_message = "There are two roots: x1 = %g, x2 = %g" % (x1, x2)
    context_dict.update({'d': d, 'message': result_message})
    return render(request, 'nine/equations.html', context_dict)


def heroes(request):
    context = {}
    context['heroes'] = get_heroes("nine/data.csv")
    return render(request, 'nine/hero.html', context)


def get_heroes(file_name, nick=None):
    heroes_list = []
    with open(file_name, 'r') as fr:
        reader_dict = csv.DictReader(fr)
        for row_dict in reader_dict:
            surname = row_dict['surname']
            name = row_dict['name']
            birthdate = row_dict['birthdate']
            nickname = row_dict['nickname'] or None
            person = Person(surname, name, birthdate, nickname)
            if nick is not None and nickname is not None:
                if nick == nickname.lower():
                    return person
            heroes_list.append(person)
    return heroes_list


class Person(object):
    """Represents notebook entry"""
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            datetime_object = datetime.strptime(birthdate, date_format)
            self.birth_date = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days // 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self. first_name)


def hero(request, nick):
    context = {}
    hero_obj = get_heroes("nine/data.csv", nick)
    context['superhero'] = hero_obj
    return render(request, 'nine/hero.html', context)
