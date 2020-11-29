from django.urls.conf import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.Celu_home, name='Celu_Home'),
    path('Prod_list', views.Prod_list , name = 'Prod_list'),
    path('Detalle_producto/<int:Producto_id>', views.Detalle_producto , name = 'Detalle_producto'),
    path('DeleteProducto/<int:Producto_id>', views.DeleteProducto , name = 'DeleteProducto'),
    path('UpdateProducto/<int:user_id>/<int:producto_id>', views.UpdateProducto , name = 'UpdateProducto'),
    path('CreateProducto/<int:user_id>', views.CreateProducto , name = 'CreateProducto'),
    path('Prod_list_Celular', views.Prod_list_Celular , name = 'Prod_list_Celular'),
    path('Prod_list_Accesorio', views.Prod_list_Accesorio , name = 'Prod_list_Accesorio'),
    re_path('Login_list2', views.Login_list2 , name = 'Login_list2'),
    re_path('Registro', views.Registro, name='Registro'),
    path('PerfilEdit/<int:user_id>', views.PerfilEdit, name='PerfilEdit'),
    path('Logout', views.logout, name='Logout'),
    re_path('ListaUsuarios', views.ListaUsuarios, name='ListaUsuarios'),
    path('Delete/<int:user_id>', views.delete, name='Delete'),
]
