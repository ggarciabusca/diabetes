from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField(primary_key=True,unique=True)
    nacimiento = models.DateField()

class Comida(models.Model):
    dni = models.IntegerField(default=0)
    dia_hora = models.DateTimeField()
    alimento = models.CharField(max_length=50)
    cantidad = models.DecimalField(decimal_places=2,max_digits=5)

class Alimentos(models.Model):
    alimento = models.CharField(max_length=50,unique=True,primary_key=True)
    carbohidratos = models.DecimalField(decimal_places=2,max_digits=6)
    racion = models.CharField(max_length=50)
    indice_glucemico = models.IntegerField(default=0)

class Medicion(models.Model):
    dni = models.ForeignKey(Persona, on_delete=models.CASCADE)
    dia_hora = models.DateTimeField()
    dato = models.IntegerField(default=0)
