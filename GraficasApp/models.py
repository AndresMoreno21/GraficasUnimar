from django.db import models

# Create your models here.

class Estudiante(models.Model):
   
    identificacion = models.CharField(max_length=100)

    ingles = models.CharField(max_length=100)
    lecturacritica = models.CharField(max_length=100)
    razonamiento  = models.CharField(max_length=100)
    competencias  = models.CharField(max_length=100)
    

    inglest = models.CharField(max_length=100, blank=True)
    lecturacriticat = models.CharField(max_length=100, blank=True)
    razonamientot  = models.CharField(max_length=100, blank=True)
    competenciast  = models.CharField(max_length=100, blank=True)
    escritot = models.CharField(max_length=100, blank=True)
    formulaciont = models.CharField(max_length=100, blank=True)
    cientificot = models.CharField(max_length=100, blank=True)
    diseñot = models.CharField(max_length=100, blank=True)

    inglesq = models.CharField(max_length=100, blank=True)
    lecturacriticaq = models.CharField(max_length=100, blank=True)
    razonamientoq  = models.CharField(max_length=100, blank=True)
    competenciasq  = models.CharField(max_length=100, blank=True)
    escritoq = models.CharField(max_length=100, blank=True)
    formulacionq = models.CharField(max_length=100, blank=True)
    cientificoq = models.CharField(max_length=100, blank=True)
    diseñoq = models.CharField(max_length=100, blank=True)

    inglese = models.CharField(max_length=100, blank=True)
    lecturacriticae = models.CharField(max_length=100, blank=True)
    razonamientoe  = models.CharField(max_length=100, blank=True)
    competenciase  = models.CharField(max_length=100, blank=True)
    escritoe = models.CharField(max_length=100, blank=True)
    formulacione = models.CharField(max_length=100, blank=True)
    cientificoe = models.CharField(max_length=100, blank=True)
    diseñoe = models.CharField(max_length=100, blank=True)

    inglesp = models.CharField(max_length=100, blank=True)
    lecturacriticap = models.CharField(max_length=100, blank=True)
    razonamientop  = models.CharField(max_length=100, blank=True)
    competenciasp  = models.CharField(max_length=100, blank=True)
    escritop = models.CharField(max_length=100, blank=True)
    formulacionp = models.CharField(max_length=100, blank=True)
    cientificop = models.CharField(max_length=100, blank=True)
    diseñop = models.CharField(max_length=100, blank=True)




