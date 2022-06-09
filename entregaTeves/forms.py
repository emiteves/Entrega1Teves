from django import forms

class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dorsal = forms.IntegerField()
    pais = forms.CharField(max_length=50)

class TecnicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    pais = forms.CharField(max_length=50)

class SeleccionFormulario(forms.Form):
    pais = forms.CharField(max_length=50)
    grupo = forms.CharField(max_length=1)