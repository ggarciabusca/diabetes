from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("login/", iniciar_sesion, name="usuarios-login"),
    path("registrar/", registrar_usuario, name="usuarios-registrar"),
]