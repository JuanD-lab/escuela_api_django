from estudiantes.models import Estudiante
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from estudiantes.serializer import EstudianteSerializer, CreateEstudianteSerializer
from django.core.mail import send_mail
from clases.permissions import ClasesPermission

# Create your views here.

class Estudiantes(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = (ClasesPermission, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateEstudianteSerializer
        
        return EstudianteSerializer

    def create(self, request, *args, **kwargs):
        print(request)
        mail = request.data['mail']
        send_mail(
            'Bienvenido',
            'Gracias por forma parte',
            'escuela@gmail.com',
            [mail],
            fail_silently=False
        )
        serializer = self.get_serializer_class()
        serialized = serializer(data=request.data)
        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        return Response(status = status.HTTP_200_OK, data= serialized.data)