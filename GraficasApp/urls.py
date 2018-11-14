from django.contrib import admin
from django.urls import path, include
from GraficasApp import views

urlpatterns = [
	
    
	path('',views.base,name='base'),
    path('Graficas/',views.graficas,name='graficas'),
    path('ListaEstudiantes/',views.estudiante_base,name='lista_estudiantes'),
    path('crearEstudiante/',views.EstudianteCreate.as_view(),name='estudiante_create'),
    path('EditarEstudiante/<int:pk>/est',views.EstudianteEditar.as_view(),name='estudiante_editar'),
    path('BorrarEstudiante/<int:pk>/est',views.EstudianteDelete.as_view(),name='estudiante_borrar'),
]