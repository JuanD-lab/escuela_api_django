from rest_framework.serializers import ModelSerializer
from estudiantes.models import Estudiante

class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'edad', 'clases')


class CreateEstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'edad', 'clases', 'mail')