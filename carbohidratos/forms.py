from django import forms

class AlimentoNuevo(forms.Form):

    #acá voy a definir los campos del formulario
    alimento = forms.CharField()
    carbohidratos = forms.DecimalField()
    racion = forms.CharField()
    indice_glucemico = forms.IntegerField()