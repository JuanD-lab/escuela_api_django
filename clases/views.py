from clases.permissions import ClasesPermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from clases.models import Clase
from clases.serializer import ClaseSerializer, CreateClaseSerializer
from estudiantes.serializer import EstudianteSerializer
from estudiantes.models import Estudiante

# Create your views here.

class Clases(ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = (ClasesPermission, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateClaseSerializer
        
        return ClaseSerializer

    def get_queryset(self):
        data = {}
        for k,v in self.request.query_params.items():
            if k == 'page':
                continue
            data[k]= v
        print(data)
        return self.queryset.filter(**data)
    
    @action(methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'], detail= True)
    def estudiantes(self, request, pk):
        clase = self.get_object()

        if request.method == 'GET':
            serialized = EstudianteSerializer(clase.estudiantes, many=True)
            return Response(
                status = status.HTTP_200_OK,
                data = serialized.data
            )
        
        if request.method in ['POST', 'PATCH', 'PUT']:
            estudiante = Estudiante.objects.get(id=request.data['estudiantes'])
            clase.estudiantes.add(estudiante)
            clase.save()
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            clase.materias.add(None)
            clase.save()
            return Response(status=status.HTTP_204_NO_CONTENT)