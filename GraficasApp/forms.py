from django import forms
from .models import *


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields= '__all__'
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'ingles': forms.TextInput(attrs={'class':'form-control'}),
            'lecturacritica': forms.TextInput(attrs={'class':'form-control'}),
            'razonamiento': forms.TextInput(attrs={'class':'form-control'}),
            'competencias': forms.TextInput(attrs={'class':'form-control'}),
            'escrito': forms.TextInput(attrs={'class':'form-control'}),
         }