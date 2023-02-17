from django.db import models

class Medico(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=50)
    matricula = models.IntegerField()
    
    def __str__(self):
       return f"Nombre: {self.nombre} \n - Apellido: {self.apellido} \n - Especialidad: {self.especialidad} \n - Matrícula: {self.matricula}"


class Paciente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    cobertura=models.CharField(max_length=50)
   
    def __str__(self):
        return f"Nombre: {self.nombre} \n - Apellido: {self.apellido} \n - Email: {self.email} \n - Cobertura: {self.cobertura}" 


class Estudios(models.Model):
    nombre= models.CharField(max_length=60)
    costo= models.IntegerField()
    
    def __str__(self):
       return f"Nombre: {self.nombre} \n - Costo: {self.costo}" 
    
    
    




