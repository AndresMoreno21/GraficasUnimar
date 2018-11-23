from django import forms
from .models import *


class EstudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields= '__all__'
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),

            'ingles': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacritica': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamiento': forms.NumberInput(attrs={'class':'form-control'}),
            'competencias': forms.NumberInput(attrs={'class':'form-control'}),
                        
            'inglest': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticat': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientot': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciast': forms.NumberInput(attrs={'class':'form-control'}),
            'escritot': forms.NumberInput(attrs={'class':'form-control'}),
            'formulaciont' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificot': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñot'  :forms.NumberInput(attrs={'class':'form-control'}),

            
            'inglesq': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticaq': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientoq': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciasq': forms.NumberInput(attrs={'class':'form-control'}),
            'escritoq': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacionq' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificoq': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñoq'  :forms.NumberInput(attrs={'class':'form-control'}),

            'inglese': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticae': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientoe': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciase': forms.NumberInput(attrs={'class':'form-control'}),
            'escritoe': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacione' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificoe': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñoe'  :forms.NumberInput(attrs={'class':'form-control'}),

            'inglesp': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticap': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientop': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciasp': forms.NumberInput(attrs={'class':'form-control'}),
            'escritop': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacionp' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificop': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñop'  :forms.NumberInput(attrs={'class':'form-control'}),
        }
    
    def clean_identificacion(self):
        identificacion = self.cleaned_data.get("identificacion")
        if Estudiante.objects.filter(identificacion=identificacion).exists():
            raise forms.ValidationError("Ya existe un estudiante con la identificacion ingresada.")
        return identificacion

class EstudianteEditarForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields= '__all__'
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),

            'ingles': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacritica': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamiento': forms.NumberInput(attrs={'class':'form-control'}),
            'competencias': forms.NumberInput(attrs={'class':'form-control'}),
                        
            'inglest': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticat': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientot': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciast': forms.NumberInput(attrs={'class':'form-control'}),
            'escritot': forms.NumberInput(attrs={'class':'form-control'}),
            'formulaciont' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificot': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñot'  :forms.NumberInput(attrs={'class':'form-control'}),

            
            'inglesq': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticaq': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientoq': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciasq': forms.NumberInput(attrs={'class':'form-control'}),
            'escritoq': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacionq' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificoq': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñoq'  :forms.NumberInput(attrs={'class':'form-control'}),

            'inglese': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticae': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientoe': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciase': forms.NumberInput(attrs={'class':'form-control'}),
            'escritoe': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacione' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificoe': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñoe'  :forms.NumberInput(attrs={'class':'form-control'}),

            'inglesp': forms.NumberInput(attrs={'class':'form-control'}),
            'lecturacriticap': forms.NumberInput(attrs={'class':'form-control'}),
            'razonamientop': forms.NumberInput(attrs={'class':'form-control'}),
            'competenciasp': forms.NumberInput(attrs={'class':'form-control'}),
            'escritop': forms.NumberInput(attrs={'class':'form-control'}),
            'formulacionp' :forms.NumberInput(attrs={'class':'form-control'}),
            'cientificop': forms.NumberInput(attrs={'class':'form-control'}),
            'diseñop'  :forms.NumberInput(attrs={'class':'form-control'}),
        }