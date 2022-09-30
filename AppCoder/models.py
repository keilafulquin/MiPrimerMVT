from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    num = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    nacimiento = models.DateField()
    email = models.EmailField()