from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate #funcines necesarias
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from usuarios.forms import UserRegisterForm

#importo el BASE_DIR del proyecto para manejar archivos
from diabetes.settings import BASE_DIR
#e importo el paquete os para manejar nombres de archivo
import os

#Defino la función para iniciar sesión
def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST) #así me lo pide el formulario de django (AuthenticationForm)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"]) #la función autehenticate devuelve un objeto de la clase "user" o un None

            #si el usuario existe
            if user is not None: 
                #vamos a hacer el login
                login(request, user) 
                return redirect("carbohidratos-inicio")
            
            #si el usuario NO existe
            else:
                return render(request, "usuarios/login.html", {"form":formulario, "errors": "Credenciales no validas"})
        else:
            return render(request, "usuarios/login.html", {"form":formulario, "errors": formulario.errors})
    
    formulario = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form":formulario, "errors":errors})

#Creamos una vista para el registro de un usuario nuevo
def registrar_usuario(request):
    errors = ""
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("carbohidratos-inicio")
        else:
            return render(request,"usuarios/registrar_usuario.html", {"form":formulario, "errors": errors})
            
    formulario = UserRegisterForm()
    return render(request, "usuarios/registrar_usuario.html", {"form":formulario, "errors": errors})
