from django.db import models
from datetime import datetime

# Create your models here.
class data(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=5000)
    time = models.DateTimeField(default=datetime.now,blank=True)
