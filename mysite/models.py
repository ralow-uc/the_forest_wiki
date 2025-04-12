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
      
