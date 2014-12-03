from django.shortcuts import render

def square(request):
    context = {'latest_question_list': 0}
    return render(request, 'square.html', context)
