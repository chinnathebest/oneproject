from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from newapp.models import some_of_our_clients as soc

# Create your views here.
def show(request):
    template=loader.get_template('index.html')
    topic=soc.objects.all()
    context={ 
        'datas1':topic,
    }
    return HttpResponse(template.render(context,request))

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.object.filter(email=email).exists():
                messages.info(request,"email already here")
                return redirect('register')
            elif User.object.filter(username=username).exists():
                messages.info(request,"username teken")
                return redirect('register')
            else:
                user=User.object.create_user(username=username,email=email,password=password1)
                user.save();
                return redirect('index')
        else:
            messages.info(request,"password is not same")
            return redirect('register')
    else:
        return render(request,'register.html')