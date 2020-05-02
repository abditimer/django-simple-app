from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # The context is a dictionary mapping template variable names to Python objects.
    context = {
        'latest_question_list': latest_question_list,
    }
    # The render() function takes the request object as its first argument, 
    # a template name as its second argument and a dictionary as its optional third argument. 
    # It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # displays a question text, with no results but with a form to vote.

    # get_object_or_404, takes a model & keywords to pass to get() function to filter
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # displays results for a particular question.
    return HttpResponse(f"You are looking at the result of the question{question_id}")

def vote(request, question_id):
    # handles voting for a particular choice in a particular question.
    return HttpResponse(f"You're voting on question {question_id}")