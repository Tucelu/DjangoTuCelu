from django.http import request
from django.shortcuts import render
from .models import Celular
from django.utils import timezone

# Create your views here.

def Celu_home(request):
    return render(request, 'celu/Tucelu.html')

def Acce_list(request):
    return render(request, 'celu/Accesorios.html')

def Celu_list(request):
    return render(request, 'celu/Celu.html')

