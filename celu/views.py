from django.http import request
from django.shortcuts import render
from .models import Celular
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login, logout as do_logout, authenticate
from django.shortcuts import redirect
from celu.models import Accesorios
from .forms import PersonaForm
from django.contrib.auth.models import User



# Create your views here.

def Celu_home(request):
    return render(request, 'celu/Tucelu.html')


def Celu_list(request):
    celulares = Celular.objects.all()
    return render(request, 'celu/Celu.html', {'celulares': celulares})

def Acce_list(request):
    accesorios = Accesorios.objects.all()
    return render(request, 'celu/Accesorios.html', {'accesorios': accesorios})


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
