from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class Estudiante(models.Model):
   
    identificacion = models.CharField(max_length=100)

    ingles = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    lecturacritica = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    razonamiento  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    competencias  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] )
    

    inglest = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    lecturacriticat = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    razonamientot  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    competenciast  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    escritot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    formulaciont = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    cientificot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    diseñot = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)

    inglesq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    lecturacriticaq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    razonamientoq  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    competenciasq  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    escritoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    formulacionq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    cientificoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    diseñoq = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)

    inglese = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    lecturacriticae = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    razonamientoe  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    competenciase  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    escritoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    formulacione = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    cientificoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    diseñoe = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)

    inglesp = models.IntegerField(blank=True,validators=[MaxValueValidator(300), MinValueValidator(0)], null=True)
    lecturacriticap = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    razonamientop  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    competenciasp  = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    escritop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    formulacionp = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    cientificop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)
    diseñop = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(0)] ,blank=True,null=True)




