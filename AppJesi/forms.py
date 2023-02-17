from django import forms


class MedicoFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    matricula = forms.IntegerField()
    especialidad = forms.CharField()
    
    


