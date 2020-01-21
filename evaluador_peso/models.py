from django.db import models

class Persona(models.Model):
    nombre     =  models.CharField(max_length=80,verbose_name="Nombre")
    nickname   =  models.CharField(primary_key=True,max_length=80,verbose_name="Nickname")
    password   =  models.CharField(max_length=80,verbose_name="Password")
    peso       =  models.DecimalField(max_digits=10,decimal_places=6,verbose_name="Peso")
    estatura   =  models.DecimalField(max_digits=10,decimal_places=6,verbose_name="Estatura")


class Medidas(models.Model):
    paciente   = models.ForeignKey(Persona,on_delete=models.CASCADE,verbose_name="Paciente")
    imc        = models.IntegerField(verbose_name="Imc",blank=True,default=-1)