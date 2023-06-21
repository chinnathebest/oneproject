from django.db import models

# Create your models here.
class bitchdetails(models.Model):
    bname=models.CharField(max_length=22)
    bass=models.IntegerField()
    bbooms=models.IntegerField()
    pussytype=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.bname}"