from django.contrib import admin
from createapp.models import motherfucker
# Register your models here.
class motherfucker_admin(admin.ModelAdmin):
    list = ['name','age','address']

admin.site.register(motherfucker,motherfucker_admin)