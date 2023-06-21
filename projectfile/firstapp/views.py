from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def welcome(requst):
    message='<h1>my name is chiku chiku slim shady<h1>'
    return HttpResponse(message)
def vanakkam(requst):
    message='<h1> vanakam da mapla, chennai la irunthu <h1>'
    return HttpResponse(message)
