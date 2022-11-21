from django.shortcuts import render
from django.http import HttpResponse
from carbohidratos.models import *
from carbohidratos.forms import AlimentoNuevo

# Create your views here.

def inicio(request):
    return render(request,"carbohidratos/inicio.html")
    pass
def personas(request):
    return render(request, "carbohidratos/personas.html")

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


def alimentos(request):
    return render(request,"carbohidratos/alimentos.html")

def nuevo_alimento(request):
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
            return render(request, "carbohidratos/alimentos.html")
            
    formulario = AlimentoNuevo()
    contexto = {"formulario":formulario}
#le paso un diccionario como contexto a mi plantilla con la info que quiero
    return render(request, "carbohidratos/nuevo_alimento.html",contexto)


def alimentos_listar(request):
    lista_alimentos = Alimentos.objects.all()
    contexto = {"alimento_resultado":lista_alimentos}
    return render(request, "carbohidratos/alimentos_buscar_resultados.html",contexto)

def alimentos_buscar(request):
    
    return render(request, "carbohidratos/alimentos_buscar.html")

def alimentos_buscar_resultado(request):
    alimento_a_buscar = request.GET["alimento_a_buscar"]
    alimento_resultado = Alimentos.objects.filter(alimento__icontains=alimento_a_buscar)
    
    contexto = {"alimento_resultado":alimento_resultado}
    return render(request, "carbohidratos/alimentos_buscar_resultados.html",contexto)
