from django.db import models

# Create your models here.

class Estudiante(models.Model):
    identificacion = models.CharField(max_length=100)

    ingles = models.CharField(max_length=100)
    lecturacritica = models.CharField(max_length=100)
    razonamiento  = models.CharField(max_length=100)
    competencias  = models.CharField(max_length=100)
    escrito = models.CharField(max_length=100)

    inglest = models.CharField(max_length=100, blank=True)
    lecturacriticat = models.CharField(max_length=100, blank=True)
    razonamientot  = models.CharField(max_length=100, blank=True)
    competenciast  = models.CharField(max_length=100, blank=True)
    escritot = models.CharField(max_length=100, blank=True)

    inglesq = models.CharField(max_length=100, blank=True)
    lecturacriticaq = models.CharField(max_length=100, blank=True)
    razonamientoq  = models.CharField(max_length=100, blank=True)
    competenciasq  = models.CharField(max_length=100, blank=True)
    escritoq = models.CharField(max_length=100, blank=True)

    inglese = models.CharField(max_length=100, blank=True)
    lecturacriticae = models.CharField(max_length=100, blank=True)
    razonamientoe  = models.CharField(max_length=100, blank=True)
    competenciase  = models.CharField(max_length=100, blank=True)
    escritoe = models.CharField(max_length=100, blank=True)

    inglesp = models.CharField(max_length=100, blank=True)
    lecturacriticap = models.CharField(max_length=100, blank=True)
    razonamientop  = models.CharField(max_length=100, blank=True)
    competenciasp  = models.CharField(max_length=100, blank=True)
    escritop = models.CharField(max_length=100, blank=True)




