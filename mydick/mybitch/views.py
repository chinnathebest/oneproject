from django.http import HttpResponse
from django.template import loader
from mybitch.models import bitchdetails
from django.contrib.auth.models import User, auth
# Create your views here.
def showthebitch(request):
    template= loader.get_template('htmlfile.html')
    takeit=bitchdetails.objects.all()
    context={
        'takeit': takeit,
    }
    return HttpResponse(template.render(context,request))

def details (request,id):
    template=loader.get_template('details.html')
    takeit=bitchdetails.objects.get(id=id)
    context={
        'takeit': takeit,
                }
    return HttpResponse(template.render(context,request))

def mainpage(request):
    template=loader.get_template('main.html')
    
    return HttpResponse(template.render())