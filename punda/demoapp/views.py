from django.shortcuts import render
import datetime

# Create your views here.
def display(requst):
    date=datetime.datetime.now()
    tell_date={'display_date':date}
    return render(requst,'demoapp/htmlfile.html',context=tell_date)
