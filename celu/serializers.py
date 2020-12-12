from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Producto
from .models import Tipo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['receptor' ,'nombre', 'descripcion', 'cantidad', 'Tipo', 'valorneto']
class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ['Tipo']