from rest_framework.serializers import ModelSerializer
from maestros.models import Maestro

class MaestroSerializer(ModelSerializer):
    class Meta:
        model = Maestro
        fields = '__all__'