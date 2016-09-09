from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(req):
    return HttpResponse('Welcome to mysite!')
