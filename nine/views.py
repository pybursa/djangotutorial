# -*- coding: utf-8 -*-

from math import sqrt

from django.shortcuts import render
from django.contrib import messages


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
