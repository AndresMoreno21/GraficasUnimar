from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class Estudiante(models.Model):
   
    identificacion = models.CharField(max_length=100)

    ingles = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    lecturacritica = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    razonamiento  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    competencias  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    

    inglest = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    lecturacriticat = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    razonamientot  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    competenciast  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    escritot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    formulaciont = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    cientificot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    diseñot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)

    inglesq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    lecturacriticaq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    razonamientoq  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    competenciasq  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    escritoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    formulacionq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    cientificoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    diseñoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)

    inglese = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    lecturacriticae = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    razonamientoe  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    competenciase  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    escritoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    formulacione = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    cientificoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    diseñoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)

    inglesp = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    lecturacriticap = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    razonamientop  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    competenciasp  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    escritop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    formulacionp = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    cientificop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)
    diseñop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True)




