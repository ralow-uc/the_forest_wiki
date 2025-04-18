from django.db import models

# Create your models here.
class Construccion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='construcciones/', null=True, blank=True)
    materiales = models.TextField(help_text="Separados por comas")
    descripcion = models.TextField()

    def get_materiales_list(self):
        return [m.strip() for m in self.materiales.split(",")]

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='animales/', null=True, blank=True)
    hostilidad = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='lugares/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Enemigo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='enemigos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Flora(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='flora/', null=True, blank=True)

    def __str__(self):
        return f"{self.numero} - {self.tipo}"

