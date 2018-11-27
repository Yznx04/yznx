from django.db import models

# Create your models here.
class IDcard(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    nation = models.CharField(max_length=10)
    brith = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    ID = models.CharField(max_length=18, primary_key=True)