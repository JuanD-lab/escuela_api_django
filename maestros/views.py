from maestros.serializer import MaestroSerializer
from django.shortcuts import render
from maestros.models import Maestro
from rest_framework.viewsets import ModelViewSet
from clases.permissions import ClasesPermission

# Create your views here.

class Maestros(ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer
    permission_classes = (ClasesPermission, )