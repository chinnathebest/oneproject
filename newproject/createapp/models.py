from django.db import models

# Create your models here.
class motherfucker(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address=models.CharField(max_length=300)
