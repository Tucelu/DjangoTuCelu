from django.contrib import admin
from .models import Producto, Tipo, DetalleProducto
# Register your models here.
 
admin.site.register(Producto)
admin.site.register(Tipo)
admin.site.register(DetalleProducto)
