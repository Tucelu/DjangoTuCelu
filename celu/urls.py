from django.urls import path
from . import views

urlpatterns = [
    path('', views.celu_list, name='Celu_list')
]
