from django.contrib import admin
from django.urls import path
from carbohidratos.views import *

urlpatterns = [
    path("inicio/", inicio,name="cabohidratos-inicio"),
]