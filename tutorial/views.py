from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from tutorial.models import Question, Choice
from django.contrib import messages


class Index(ListView):
    template_name = 'tutorial/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class Detail(DetailView):
    template_name = 'tutorial/detail.html'
    model = Question


class Results(DetailView):
    template_name = 'tutorial/results.html'
    model = Question


class Vote(View):
    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        try:
            choice = question.choice_set.get(pk=request.POST.get('choice'))
        except Choice.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Invalid choice")
            return redirect('tutorial:detail', pk=question.id)
        else:
            choice.votes += 1
            choice.save()
            return redirect('tutorial:results', pk=question.id)