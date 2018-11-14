from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from GraficasApp import forms
from django.urls import reverse_lazy 

# Create your views here.



def base(request):
    return render(request, 'baseAdmin.html')

def graficas(request):
    return render(request, 'graficas.html')


def estudiante_base(request):
    e = Estudiante.objects.all()
    context = {'estudiantes_list': e}
    return render(request, 'ListaEstudiantes.html', context)

class EstudianteCreate(CreateView):
    model = Estudiante
    form_class = forms.EstudianteForm
    template_name = 'estudianteCreate.html'
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteEditar(UpdateView):
    model = Estudiante
    form_class = forms.EstudianteForm
    template_name = 'estudianteEditar.html'
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'estudiante_confirm_delete.html'
    success_url = reverse_lazy('lista_estudiantes')