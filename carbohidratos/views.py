from django.shortcuts import render
from django.http import HttpResponse
from carbohidratos.models import *
from usuarios.models import *
from usuarios.views import avatar_usuario
from carbohidratos.forms import AlimentoNuevo
#from django.contrib.auth.mixins import LoginRequiredMixin esto sirve para requerir autenticación en Vistas basadas en clases
from django.contrib.auth.decorators import login_required # lo mismo que el anterior, pero para Vistas basadas en Funciones
import os
from diabetes.settings import BASE_DIR

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        if len(Avatar.objects.filter(user = request.user.id))==1:
            imagen_usuario = Avatar.objects.filter(user = request.user.id)[0]
            imagen_url = imagen_usuario.imagen.url
            print("uno", imagen_usuario)
            print("dos",imagen_url)
        else:
            imagen_url=""
    else:
        imagen_url = ""
    return render(request, "carbohidratos/inicio.html", {"avatar": imagen_url})

#def inicio(request):
#    return render(request,"carbohidratos/inicio.html")



def personas(request):
    return render(request, "carbohidratos/personas.html")

@login_required
def personas_listar(request):
    #obtengo el listado de personas de la base de datos
    lista_personas = Persona.objects.all()
    contexto = {"personas_resultado":lista_personas}

    return render(request,"carbohidratos/personas_buscar_resultados.html", contexto)

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
        return render(request, "carbohidratos/personas.html")

    return render(request, "carbohidratos/nueva_persona.html")

def comidas(request):
    return render(request,"carbohidratos/comidas.html")
    

def mediciones(request):
    return render(request,"carbohidratos/mediciones.html")

def nueva_medicion(request):
    if request.method == "POST":
        nuevo_dni= request.POST["dni"]
        nuevo_dia_hora = request.POST["dia_hora"]
        nuevo_dato = request.POST["dato"]
    
        medicion_nueva = Medicion(dni_id=nuevo_dni, dia_hora=nuevo_dia_hora, dato=nuevo_dato)
        medicion_nueva.save()
        return render(request,"carbohidratos/mediciones.html")
        
    return render(request, "carbohidratos/nueva_medicion.html")

def mediciones_buscar(request):
    return render(request, "carbohidratos/mediciones_buscar.html")
    

def mediciones_buscar_resultado(request):

    imagen_usuario = avatar_usuario(request.user)
    #obtengo el dni a buscar
    persona_a_buscar = request.GET["persona_a_buscar"]

    #obtengo de la base de datos el listado de mediciones de la persona indicada
    medidas_resultado = Medicion.objects.filter(dni_id=persona_a_buscar)
    persona = Persona.objects.filter(dni=persona_a_buscar)

    #paso como contexto el listado de las mediciones
    contexto = {"nombre":persona[0].nombre,"apellido":persona[0].apellido, "medidas_resultado":medidas_resultado,"avatar":imagen_usuario}
    return render(request,"carbohidratos/mediciones_buscar_resultados.html", contexto)

def alimentos(request):
    
    imagen_usuario = avatar_usuario(request.user)
    return render(request,"carbohidratos/alimentos.html",{"avatar":imagen_usuario})

def nuevo_alimento(request):
    imagen_usuario = avatar_usuario(request.user)
    #si la petición es de tipo POST
    if request.method == "POST":
        
        #cargo los datos
        formulario = AlimentoNuevo(request.POST)

        #valido que el formulario tenga datos válidos
        if formulario.is_valid():
        
            #recupero los datos del formulario hacia una variable llamada "datos"
            datos = formulario.cleaned_data
        
            #y creo el alimento en la base de datos
            alimento_nuevo = Alimentos(alimento=datos["alimento"], carbohidratos=datos["carbohidratos"], racion=datos["racion"], indice_glucemico=datos["indice_glucemico"])
            alimento_nuevo.save()
            return render(request, "carbohidratos/alimentos.html",{"avatar":imagen_usuario})
            
    formulario = AlimentoNuevo()
    contexto = {"formulario":formulario,"avatar":imagen_usuario}
#le paso un diccionario como contexto a mi plantilla con la info que quiero
    return render(request, "carbohidratos/nuevo_alimento.html",contexto)


def alimentos_listar(request):

    lista_alimentos = Alimentos.objects.all()
    contexto = {"alimento_resultado":lista_alimentos,"avatar":avatar_usuario(request.user)}
    return render(request, "carbohidratos/alimentos_buscar_resultados.html",contexto)

def alimentos_buscar(request):
    
    return render(request, "carbohidratos/alimentos_buscar.html",{"avatar":avatar_usuario(request.user)})

def alimentos_buscar_resultado(request):
    alimento_a_buscar = request.GET["alimento_a_buscar"]
    alimento_resultado = Alimentos.objects.filter(alimento__icontains=alimento_a_buscar)
    
    contexto = {"alimento_resultado":alimento_resultado,"avatar":avatar_usuario(request.user)}
    return render(request, "carbohidratos/alimentos_buscar_resultados.html",contexto)
