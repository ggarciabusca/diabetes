from django.contrib import admin
from django.urls import path
from carbohidratos.views import *

urlpatterns = [
    path("inicio/", inicio, name="carbohidratos-inicio"),
    path("personas/", personas, name="carbohidratos-personas"),
    path("personas/buscar/resultados/", personas_listar, name="carbohidratos-personas-buscar-resultados"),
    path("personas/nueva/", nueva_persona, name="carbohidratos-personas-nueva"),
    path("comidas/", comidas, name="carbohidratos-comidas"),
    path("mediciones/", mediciones, name="carbohidratos-mediciones"),
    path("mediciones/nueva/", nueva_medicion, name="carbohidratos-mediciones-nueva"),
    path("mediciones/buscar/", mediciones_buscar, name="carbohidratos-mediciones-buscar"),
    path("mediciones/buscar/resultados/", mediciones_buscar_resultado, name="carbohidratos-mediciones-buscar-resultados"),
    path("alimentos/", alimentos, name="carbohidratos-alimentos"),
    path("alimentos/nuevo/", nuevo_alimento, name="carbohidratos-alimentos-nuevo"),
    path("alimentos/listar/", alimentos_listar, name="carbohidratos-alimentos-listar"),
    path("alimentos/buscar/", alimentos_buscar, name="carbohidratos-alimentos-buscar"),
    path("alimentos/buscar/resultados/", alimentos_buscar_resultado, name="carbohidratos-alimentos-buscar-resultados")
]
