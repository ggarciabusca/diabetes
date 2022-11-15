from django.shortcuts import render
from django.http import HttpResponse
from carbohidratos.models import *

# Create your views here.

def inicio(request):
    return render(request,"carbohidratos/base.html")
    pass

def personas(request):
    return render(request,"carbohidratos/personas.html")
    pass

def comidas(request):
    return render(request,"carbohidratos/comidas.html")
    pass

def mediciones(request):
    return render(request,"carbohidratos/mediciones.html")
    pass

def alimentos(request):
    return render(request,"carbohidratos/alimentos.html")
    pass