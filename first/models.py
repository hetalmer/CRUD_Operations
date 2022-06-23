from statistics import mode
from django.db import models

# Create your models here.
class First(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)