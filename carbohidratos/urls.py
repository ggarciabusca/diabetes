from django.contrib import admin
from django.urls import path
from carbohidratos.views import *

urlpatterns = [
    path("inicio/", inicio,name="carbohidratos-inicio"),
    path("personas/", personas,name="carbohidratos-personas"),
    path("comidas/", comidas,name="carbohidratos-comidas"),
    path("mediciones/", mediciones,name="carbohidratos-mediciones"),
    path("alimentos/", alimentos,name="carbohidratos-alimentos")
]