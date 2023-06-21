from django.db import models

# Create your models here.
class some_of_our_clients(models.Model):
    name=models.CharField(max_length=50)
    discription=models.CharField(max_length=200)

    