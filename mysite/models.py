from django.db import models
from django.contrib.auth.models import AbstractUser
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
      

from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_grupo',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permisos',
        blank=True,
    )

    def __str__(self):
        return self.username
