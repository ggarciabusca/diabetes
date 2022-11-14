from django.shortcuts import render
from django.http import HttpResponse
from carbohidratos.models import *

# Create your views here.

def inicio(request):
    return render(request,"carbohidratos/index.html")
    pass