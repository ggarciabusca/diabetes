from django.shortcuts import render
from django.http import HttpResponse
from carbohidratos.models import *

# Create your views here.

def inicio(request):
    return render(request,"carbohidratos/base.html")
    pass

def personas(request):
    #obtengo el listado de personas de la base de datos
    lista_personas = Persona.objects.all()

    return render(request,"carbohidratos/personas.html")

def nueva_persona(request):
    #acá me traigo los datos desde el formulario y los guardo en variables para luego crear la instancia
    if request.method == "POST":
        nombre_nuevo = request.POST["nombre"]
        apellido_nuevo = request.POST["apellido"]
        dni_nuevo = request.POST["dni"]
        nacimiento_nuevo = request.POST["nacimiento"]
        
        #creo una instancia llamada "persona_nueva" de la clase "Persona" con los atributos que traigo desde el formulario
        persona_nueva = Persona(nombre=nombre_nuevo, apellido=apellido_nuevo, dni=dni_nuevo, nacimiento=nacimiento_nuevo)
        persona_nueva.save() #con esto lo guardo en la base de datos

    return render(request, "carbohidratos/nueva_persona.html")

def comidas(request):
    return render(request,"carbohidratos/comidas.html")
    pass

def mediciones(request):
    return render(request,"carbohidratos/mediciones.html")

def nueva_medicion(request):
    if request.method == "POST":
        nuevo_dni= request.POST["dni_mediciones"]
        nuevo_dia_hora = request.POST["dia_hora_mediciones"]
        nuevo_dato = request.POST["dato"]
    
        medicion_nueva = Medicion(dni=nuevo_dni, dia_hora=nuevo_dia_hora, dato=nuevo_dato)
        medicion_nueva.save()
    return render(request, "carbohidratos/nueva_medicion.html")

    
def alimentos(request):
    return render(request,"carbohidratos/alimentos.html")
    pass