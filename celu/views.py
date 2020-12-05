from django.http import request
from django.shortcuts import render
from .models import Producto, Tipo
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login, logout as do_logout, authenticate
from django.shortcuts import redirect
from .forms import PersonaForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from celu import forms
from django.contrib import messages
import os



# Create your views here.

def Celu_home(request):
    return render(request, 'celu/Tucelu.html')


def Prod_list_Celular(request):
    productos = Producto.objects.filter(Tipo = 1)
    return render(request, 'CrudProductos/ReadandDeleteProductos.html', {'productos': productos})

def Prod_list_Accesorio(request):
    productos = Producto.objects.filter(Tipo = 2)
    return render(request, 'CrudProductos/ReadandDeleteProductos.html', {'productos': productos})

def Detalle_producto(request, Producto_id):
    producto = Producto.objects.filter(id = Producto_id)
    return render(request, 'celu/Detalle_producto.html', {'producto': producto})



def Login_list2(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'celu/Login.html', {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

# C = Create
def Registro(request):
    # Creamos el formulario de autenticación vacío
    form = PersonaForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PersonaForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "celu/Registro.html", {'form': form})

#R = READ
@login_required
def ListaUsuarios(request):
    usuario = User.objects.all()
    context = {'usuario': usuario}
    return render(request, 'celu/ListaUsuarios.html', context)

#U = UPDATE
@login_required
def PerfilEdit(request, user_id):
    # Recuperamos la instancia de la persona
    instancia = User.objects.get(id = user_id)
    # Creamos el formulario de autenticación vacío
    form = PersonaForm(instance = instancia)
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = PersonaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            instancia.save()


    # Si llegamos al final renderizamos el formulario
    return render(request, "celu/Perfil.html", {'form': form})

#D = DELETE
@login_required
def delete(request, user_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = User.objects.get(id=user_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/')


#C = Create --- Productos
@login_required
def CreateProducto(request, user_id):
    tiposubida = int

    if request.POST:
        producto = Producto()
        tiposubida = User.objects.get(id= user_id)
        producto.receptor = tiposubida
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.cantidad = request.POST.get('cantidad')
        producto.valorneto = request.POST.get('valorneto')
        producto.foto = request.FILES.get('foto')
        if (request.POST.get('Tipo') == 'Celular'):
            tiposubida = 1
        else:
            tiposubida  = 2
        producto.Tipo = Tipo.objects.get(id = tiposubida )

        producto.save()
        return redirect('/')
        
    return render(request, "CrudProductos/CreateProducto.html")
#R = Read --- Productos
def Prod_list(request):
    productos = Producto.objects.all()
    return render(request, 'CrudProductos/ReadandDeleteProductos.html', {'productos': productos})

#U = Update --- Productos
@login_required
def UpdateProducto(request, user_id, producto_id):

    Productoamodificar = Producto.objects.filter(id = producto_id)
    tiposubida = int
    productotemporal = Producto()
    if request.POST:
        for productoo in Productoamodificar:
            productoo.pk = producto_id

            tiposubida = User.objects.get(id= user_id)

            productoo.receptor = tiposubida

            productoo.nombre = request.POST.get('nombre')

            productoo.descripcion = request.POST.get('descripcion')

            productoo.cantidad = request.POST.get('cantidad')

            productoo.valorneto = request.POST.get('valorneto')

            if request.FILES.get('foto') != None:
                productoo.foto = request.FILES.get('foto')


            if (request.POST.get('Tipo') == 'Celular'):
                tiposubida = 1
            else:
                tiposubida  = 2
            productoo.Tipo = Tipo.objects.get(id = tiposubida )

            productoo.save()
            return redirect('/')
    return render(request, "CrudProductos/UpdateProducto.html",{'Productoamodificar': Productoamodificar})

#D = Delete --- Productos
@login_required
def DeleteProducto(request, Producto_id):
    # Recuperamos la instancia de la persona y la borramos
    producto = Producto.objects.get(id=Producto_id)
    producto.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('Prod_list')