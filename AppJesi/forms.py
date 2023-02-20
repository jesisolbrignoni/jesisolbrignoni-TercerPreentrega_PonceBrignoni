from django import forms


class MedicoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    matricula = forms.IntegerField()
    especialidad = forms.CharField()
    
class EstudiosFormulario(forms.Form):
    nombre = forms.CharField()
    costo = forms.IntegerField()
    
class PacienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    cobertura = forms.CharField()   
    


