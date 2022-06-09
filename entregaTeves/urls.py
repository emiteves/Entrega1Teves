
from django.urls import path
from entregaTeves import views
from entregaTeves.views import inicio, futbolistas, futbolistaFormulario, tecnicos, selecciones, buscar, busquedaporPais, tecnicoFormulario, seleccionFormulario



urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('futbolistas/', futbolistas, name = 'futbolistas'),
    path('tecnicos/', tecnicos, name = 'tecnicos'),
    path('selecciones/', selecciones, name = 'selecciones'),
    path('futbolistaFormulario/', futbolistaFormulario, name = 'futbolistaFormulario'),
    path('tecnicoFormulario/', tecnicoFormulario, name = 'tecnicoFormulario'),
    path('seleccionFormulario/', seleccionFormulario, name = 'seleccionFormulario'),
    path('buscar/', buscar , name = 'buscar'),
    path('busquedaporPais/', busquedaporPais, name='busquedaporPais'),
    

]
