from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from server.models import Ancho
from server.serializers.anchoSerializer import anchoSerializer


class anchoViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Ancho.objects.all()
    serializer_class = anchoSerializer
