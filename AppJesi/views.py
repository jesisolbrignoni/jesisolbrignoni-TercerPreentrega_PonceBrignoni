from django.shortcuts import render
from django.http import HttpResponse
from AppJesi.models import *
from AppJesi.forms import MedicoFormulario, EstudiosFormulario, PacienteFormulario

def inicio(request):
    return render(request, 'AppJesi/inicio.html')


def pacientes(request):
    if request.method == 'POST':
        miFormulario = PacienteFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], cobertura=informacion['cobertura'])
            paciente.save()
            return render(request, "AppJesi/inicio.html")
    else:
        miFormulario = PacienteFormulario()
            
    return render(request, "AppJesi/pacienteFormulario.html", {"miFormulario":miFormulario})


def estudios(request):
    if request.method == 'POST':
        miFormulario = EstudiosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudio = Estudios(nombre=informacion['nombre'], costo=informacion['costo'])
            estudio.save()
            return render(request, "AppJesi/inicio.html")
    else:
        miFormulario = EstudiosFormulario()
            
    return render(request, "AppJesi/estudiosFormulario.html", {"miFormulario":miFormulario})


def medicos(request):
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

#def busqueda_medico(request):
#    return render(request, "AppJesi/busqueda_medico.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        medicos = Medico.objects.filter(nombre__icontains=nombre)
    
        return render(request, "AppJesi/inicio.html", {"medicos":medicos, "nombre":nombre})
    
    else:
        respuesta = "No enviaste datos" 

    return HttpResponse(respuesta)
    