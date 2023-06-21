from django.shortcuts import render
from .models import data

# Create your views here.
def main_page(request):
    info=data.objects.all()
    return render(request,"index.html",{'data':info})

def sub_page(request,pk):
    info=data.objects.get(id=pk)
    return render(request,"page.html",{'data':info})