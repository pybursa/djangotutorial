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
    d = get_discr(**context_dict)
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
