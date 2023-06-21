from django.contrib import admin
from mybitch.models import bitchdetails

# Register your models here.
class bitchadmin(admin.ModelAdmin):
    list_display=("bname","bass","pussytype")
    
admin.site.register(bitchdetails,bitchadmin)