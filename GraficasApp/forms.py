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
            
            

            
            'inglest': forms.TextInput(attrs={'class':'form-control'}),
            'lecturacriticat': forms.TextInput(attrs={'class':'form-control'}),
            'razonamientot': forms.TextInput(attrs={'class':'form-control'}),
            'competenciast': forms.TextInput(attrs={'class':'form-control'}),
            'escritot': forms.TextInput(attrs={'class':'form-control'}),
            'formulaciont' :forms.TextInput(attrs={'class':'form-control'}),
            'cientificot': forms.TextInput(attrs={'class':'form-control'}),
            'diseñot'  :forms.TextInput(attrs={'class':'form-control'}),

            
            'inglesq': forms.TextInput(attrs={'class':'form-control'}),
            'lecturacriticaq': forms.TextInput(attrs={'class':'form-control'}),
            'razonamientoq': forms.TextInput(attrs={'class':'form-control'}),
            'competenciasq': forms.TextInput(attrs={'class':'form-control'}),
            'escritoq': forms.TextInput(attrs={'class':'form-control'}),
            'formulacionq' :forms.TextInput(attrs={'class':'form-control'}),
            'cientificoq': forms.TextInput(attrs={'class':'form-control'}),
            'diseñoq'  :forms.TextInput(attrs={'class':'form-control'}),

            'inglese': forms.TextInput(attrs={'class':'form-control'}),
            'lecturacriticae': forms.TextInput(attrs={'class':'form-control'}),
            'razonamientoe': forms.TextInput(attrs={'class':'form-control'}),
            'competenciase': forms.TextInput(attrs={'class':'form-control'}),
            'escritoe': forms.TextInput(attrs={'class':'form-control'}),
            'formulacione' :forms.TextInput(attrs={'class':'form-control'}),
            'cientificoe': forms.TextInput(attrs={'class':'form-control'}),
            'diseñoe'  :forms.TextInput(attrs={'class':'form-control'}),

            
            'inglesp': forms.TextInput(attrs={'class':'form-control'}),
            'lecturacriticap': forms.TextInput(attrs={'class':'form-control'}),
            'razonamientop': forms.TextInput(attrs={'class':'form-control'}),
            'competenciasp': forms.TextInput(attrs={'class':'form-control'}),
            'escritop': forms.TextInput(attrs={'class':'form-control'}),
            'formulacionp' :forms.TextInput(attrs={'class':'form-control'}),
            'cientificop': forms.TextInput(attrs={'class':'form-control'}),
            'diseñop'  :forms.TextInput(attrs={'class':'form-control'}),
         }