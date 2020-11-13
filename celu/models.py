from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

class Celular(models.Model):
    receptor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    sistemaoperativo = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200, null=True)
    cantidad = models.IntegerField()
    valorneto = models.IntegerField()
    fecharecepcion = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to= 'Celulares')

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.modelo


class Accesorios(models.Model):
    receptor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200, null=True)
    cantidad = models.IntegerField()
    valorneto = models.IntegerField()
    fecharecepcion = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to= 'Accesorios')

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.Nombre
