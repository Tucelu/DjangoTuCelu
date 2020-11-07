from django.urls.conf import path
from django.urls import re_path
from . import views

urlpatterns = [
    
    path('', views.Celu_home, name='Celu_Home'),
    path('Acce_list', views.Acce_list , name = 'Acce_list'),
    path('Celu_list', views.Celu_list , name = 'Celu_list'),
    path('Login_list', views.Celu_list , name = 'Login_list'),
    
]
