from django.urls import path
from AppJesi import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('medicos', views.medicos, name = "Medicos"),
    path('pacientes', views.pacientes, name = "Pacientes"),
    path('estudios', views.estudios, name = "Estudios"),
    path('medicoFormulario', views.medicoFormulario, name="medicoFormulario"),
]