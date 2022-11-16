from django.contrib import admin
from django.urls import path
from carbohidratos.views import *

urlpatterns = [
    path("inicio/", inicio, name="carbohidratos-inicio"),
    path("personas/", personas, name="carbohidratos-personas"),
    path("personas/nueva/", nueva_persona, name="carbohidratos-personas-nueva"),
    path("comidas/", comidas, name="carbohidratos-comidas"),
    path("mediciones/", mediciones, name="carbohidratos-mediciones"),
    path("mediciones/nueva/", nueva_medicion, name="carbohidratos-mediciones-nueva"),
    path("alimentos/", alimentos, name="carbohidratos-alimentos")
]