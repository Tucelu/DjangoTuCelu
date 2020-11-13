from django.urls.conf import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.Celu_home, name='Celu_Home'),
    re_path('Acce_list', views.Acce_list , name = 'Acce_list'),
    re_path('Celu_list', views.Celu_list , name = 'Celu_list'),
    re_path('Login_list2', views.Login_list2 , name = 'Login_list2'),
    re_path('Registro', views.Registro, name='Registro'),
    re_path('PerfilEdit/<int:user_id>', views.PerfilEdit, name='PerfilEdit'),
    re_path('Logout', views.logout, name='logout'),
    re_path('ListaUsuarios', views.ListaUsuarios, name='ListaUsuarios'),
    re_path('Delete/<int:user_id>', views.delete, name='Delete'),
]
