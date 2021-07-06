from django.db import models
from django.db.models.deletion import CASCADE
from django import forms


# Create your models here.
class inicio_sesion(models.Model):
    correo = models.IntegerField(primary_key=True, verbose_name='correo')

    def __str__(self):
        return(self.correo)

    def __str__(self):
        return(self.nombre)

class Colab(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre Completo')
    pais = models.CharField(max_length=20, verbose_name='Pais')
    region = models.CharField(max_length=20, verbose_name='Region')
    direccion = models.CharField(max_length=60, verbose_name='Direccion')
    telefono = models.CharField(max_length=60, verbose_name='Telefono')
    email= models.CharField(max_length=60, verbose_name='Email')
    contrasena = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return(self.rut)



        

