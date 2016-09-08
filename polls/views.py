from django.http import HttpResponse

def index(req):
    return HttpResponse('Hello, world. You\'re at the polls index.')

def detail(req, question_id):
    res = 'You\'re looking at the results of question %s.'
    return HttpResponse(res % question_id)

def vote(req, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)
