from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome),
    path('vanakkam/',views.vanakkam)
]
