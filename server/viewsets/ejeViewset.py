from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from server.models import Eje
from server.serializers.ejeSerializer import ejeSerializer


class ejeViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Eje.objects.all()
    serializer_class = ejeSerializer