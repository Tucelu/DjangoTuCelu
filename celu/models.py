from django.db import models
from django.utils import timezone

# Create your models here.

class Celulares(models.Model):
    receptor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200)
    marca = models.TextField()
    sistemaoperativo = models.TextField()
    color = models.TextField()
    cantidad = models.IntegerField()
    valorneto = models.IntegerField()
    fecharecepcion = models.DateField(blank=True, null=True)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.modelo
            