from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from entregaTeves.models import Futbolistas, Selecciones, Tecnicos
from entregaTeves.forms import FutbolistaFormulario, TecnicoFormulario, SeleccionFormulario


def futbolistas(request):
    futbolistas = Futbolistas.objects.all().order_by('pais')
    contexto = {"Futbolistas":futbolistas}
    return render(request, 'entregaTeves/futbolistas.html', contexto)

def selecciones(request):
    selecciones = Selecciones.objects.all().order_by('grupo')
    contexto = {"Selecciones":selecciones}
    return render(request, 'entregaTeves/selecciones.html', contexto)

def tecnicos(request):
    tecnicos = Tecnicos.objects.all().order_by('pais')
    contexto = {"Tecnicos":tecnicos}
    return render(request, 'entregaTeves/tecnicos.html', contexto)

def inicio(request):
    plantilla = loader.get_template('entregaTeves/padre.html')
    documento = plantilla.render()
    return HttpResponse(documento)

# Formularios insertar informacion base de datos

def futbolistaFormulario (request):
    if request.method == 'POST':
        miFormulario = FutbolistaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            dorsal = informacion ['dorsal']
            pais = informacion ['pais']
            futbolista = Futbolistas (nombre =nombre, apellido =apellido, dorsal =dorsal, pais = pais)
            futbolista.save()
        return render(request, 'entregaTeves/inicio.html')
    else:
        miFormulario = FutbolistaFormulario()
    return render (request, 'entregaTeves/futbolistaFormulario.html', {'miFormulario':miFormulario})

def tecnicoFormulario (request):
    if request.method == 'POST':
        miFormulario = TecnicoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            pais = informacion ['pais']
            tecnico = Tecnicos (nombre =nombre, apellido =apellido, pais = pais)
            tecnico.save()
        return render(request, 'entregaTeves/inicio.html')
    else:
        miFormulario = TecnicoFormulario()
    return render (request, 'entregaTeves/tecnicoFormulario.html', {'miFormulario':miFormulario})

def seleccionFormulario (request):
    if request.method == 'POST':
        miFormulario = SeleccionFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            grupo = informacion ['grupo']
            pais = informacion ['pais']
            seleccion = Selecciones (grupo =grupo, pais = pais)
            seleccion.save()
        return render(request, 'entregaTeves/inicio.html')
    else:
        miFormulario = SeleccionFormulario()
    return render (request, 'entregaTeves/seleccionFormulario.html', {'miFormulario':miFormulario})

###### Busqueda por pais

def busquedaporPais(request):
    return render(request, 'entregaTeves/busquedaporPais.html')

def buscar(request):

    if request.GET['pais']:
        pais = request.GET['pais']
        futbolistas = Futbolistas.objects.filter(pais = pais).order_by('dorsal')
        tecnicos = Tecnicos.objects.filter(pais = pais)
        selecciones = Selecciones.objects.filter(pais = pais)
        return render(request, 'entregaTeves/resultadoBusquedaporPais.html', {'futbolistas':futbolistas, 'pais' : pais, 'tecnicos': tecnicos, 'selecciones':selecciones})
    else:
        respuesta = "Ingrese datos correctamente"
    return HttpResponse(respuesta)

##### 

### def listafutbolistas(request):
    futbolista_list = Futbolistas.objects.all()
    return render(request, 'futbolistas.html', {'futbolista' : futbolista_list})