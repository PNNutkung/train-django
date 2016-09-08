from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, req))

def detail(req, question_id):
    return HttpResponse('You\'re looking at question %s.'% question_id)

def results(req, question_id):
    res = 'You\'re looking at the results of question %s.'
    return HttpResponse(res % question_id)

def vote(req, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)
