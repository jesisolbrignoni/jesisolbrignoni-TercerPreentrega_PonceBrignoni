from django.shortcuts import render
from django.http import HttpResponse
from AppJesi.models import *
from AppJesi.forms import MedicoFormulario

#def estudio(self):
#    estudio = Estudios(nombre='Análisis de Laboratorio', costo="4000")
#   estudio.save()
#   documento_de_texto = f"- Estudio: {estudio.nombre} - Costo: {estudio.costo}"
#   return HttpResponse(documento_de_texto)

def inicio(request):
    return render(request, 'AppJesi/inicio.html')
    #return HttpResponse('vista inicio')

def medicos(request): 
    return render(request, 'AppJesi/medicos.html')
    #return HttpResponse('vista medicos')

def pacientes(request):
    return render(request, 'AppJesi/pacientes.html')
    #return HttpResponse('vista pacientes')

def estudios(request): 
    return render(request, 'AppJesi/estudios.html')
    #return HttpResponse('vista estudios')
    
#def medicoFormulario(request):
#   if request.method == 'POST':
#        medico = Medico(request.POST['nombre'], request.POST['apellido'], request.POST['matricula'], request.POST['especialidad'])
#       medico.save()
#       return render(request, "AppJesi/inicio.html")
#   return render(request, "AppJesi/medicoFormulario.html")

def medicoFormulario(request):
    if request.method == 'POST':
        miFormulario = MedicoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'], matricula=informacion['matricula'], especialidad=informacion['especialidad'])
            medico.save()
            return render(request, "AppJesi/inicio.html")
    else:
        miFormulario = MedicoFormulario()
            
    return render(request, "AppJesi/medicoFormulario.html", {"miFormulario":miFormulario})

