from django.urls import path
from AppJesi import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('medicos', views.medicos, name = "Medicos"),
    path('pacientes', views.pacientes, name = "Pacientes"),
    path('estudios', views.estudios, name = "Estudios"),
    #path('busqueda_medico', views.busqueda_medico, name = "busqueda_medico"),
    path('buscar/', views.buscar),
]