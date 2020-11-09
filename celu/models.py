from django.db import models
from django.utils import timezone
from django import forms    
from django.contrib.auth.models import User # fill in custom user info then save it 

# Create your models here.

class Celular(models.Model):
    receptor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200)
    marca = models.TextField(max_length=30)
    sistemaoperativo = models.TextField(max_length=100)
    color = models.TextField(max_length=15)
    cantidad = models.IntegerField()
    valorneto = models.IntegerField()
    fecharecepcion = models.DateField(blank=True, null=True)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.modelo
