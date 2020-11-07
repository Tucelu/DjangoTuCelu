from django.urls.conf import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.celu_home, name='Celu_Home'),
    path('', views.celu_list, name='Celu_list')
  
]
