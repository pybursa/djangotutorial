# -*- coding: utf-8 -*-

import csv
from math import sqrt

from django.shortcuts import render
from django.contrib import messages
from django.http import Http404


def square(request):
    roots = []
    params = get_params(request)

    if params.__len__() is 3:
        a, b, c = params[0], params[1], params[2]
        d = b ** 2 - 4 * a * c
        if d > 0:
            roots.append((-b + sqrt(d)) / (2 * a))
            roots.append((-b - sqrt(d)) / (2 * a))
        elif d is 0:
            roots.append(-b / (2 * a))
        else:
            messages.add_message(request, messages.INFO, 'Корней нет')

    return render(request, 'nine/square.html', {
        'roots': roots,
    })


def get_params(request):
    result = []

    a = request.GET.get('a')
    if a is None or not a.isdigit() or a == '0':
        err(request, 'Неправильный параметр a')
    else:
        result.append(int(a))

    b = request.GET.get('b')
    if b is None or not b.isdigit():
        err(request, 'Неправильный параметр b')
    else:
        result.append(int(b))

    c = request.GET.get('c')
    if c is None or not c.isdigit():
        err(request, 'Неправильный параметр c')
    else:
        result.append(int(c))

    return result


def err(request, msg):
    messages.add_message(request, messages.ERROR, msg)


def heroes(request):
    with open('nine/data.csv', 'r') as data:
        data = list(csv.reader(data))
        return render(request, 'nine/heroes.html', {
            'header': data[0],
            'data': data[1:],
        })


def detail(request, nickname):
    with open('nine/data.csv', 'r') as data:
        data = list(csv.reader(data))
        hero = None
        for i in data[1:]:
            if i[5].lower() == nickname.lower():
                hero = i
                break

        if hero is not None:
            return render(request, 'nine/detail.html', {
                'data': zip(data[0], hero),
            })

        raise Http404
