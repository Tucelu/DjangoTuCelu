from django.shortcuts import render
from .models import Celular
from django.utils import timezone

# Create your views here.

def celu_list(request):
    celu = Celular.objects.all()
    return render(request, 'celu/Celu.html', {'celu': celu})