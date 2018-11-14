from django.db import models

# Create your models here.

class Estudiante(models.Model):
    identificacion = models.CharField(max_length=100)
    ingles = models.CharField(max_length=100)
    lecturacritica = models.CharField(max_length=100)
    razonamiento  = models.CharField(max_length=100)
    competencias  = models.CharField(max_length=100)
    escrito = models.CharField(max_length=100)




