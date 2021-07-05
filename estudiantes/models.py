from django.db import models
from clases.models import Clase

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    mail = models.CharField(max_length=200)
    clases = models.ManyToManyField(
        Clase,
        related_name='estudiantes'
    )

    def __str__(self):
        return self.nombre