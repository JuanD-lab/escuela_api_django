from django.db import models
from maestros.models import Maestro
# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    maestro = models.ForeignKey(
        Maestro,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre