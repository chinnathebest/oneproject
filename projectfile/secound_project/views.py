from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def telltime(requst):
    time=datetime.datetime.now()
    return HttpResponse(time)
