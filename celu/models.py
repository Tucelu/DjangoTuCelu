from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    receptor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500, null=True)
    cantidad = models.IntegerField()
    valorneto = models.IntegerField()
    foto = models.ImageField(upload_to= 'Producto')
    Tipo = models.ForeignKey('celu.Tipo', on_delete=models.CASCADE)
    detalle_id = models.ForeignKey('celu.DetalleProducto', on_delete=models.CASCADE, null=True)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    Tipo = models.CharField(max_length=20)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.Tipo

class DetalleProducto(models.Model):
    Total_iva = models.IntegerField(null=True)
    CantidadCompras = models.IntegerField(null=True)
    Cliente_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.Total_iva

class Carrito(models.Model):
    Detalle_id = models.ForeignKey('celu.DetalleProducto', on_delete=models.CASCADE)
    Total_compra = models.IntegerField(null=True)

    def publish(self):
        self.fecharecepcion = timezone.now()
        self.save()

    def __str__(self):
        return self.Total_compra
