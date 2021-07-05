from rest_framework.serializers import ModelSerializer
from estudiantes.serializer import EstudianteSerializer
from clases.models import Clase

class ClaseSerializer(ModelSerializer):
    estudiantes = EstudianteSerializer(read_only=True, many=True)
    class Meta:
        model = Clase
        fields = ('id', 'nombre', 'maestro', 'estudiantes')


class CreateClaseSerializer(ModelSerializer):
    class Meta:
        model = Clase
        fields = ('nombre', )