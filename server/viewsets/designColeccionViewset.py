from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from server.models import Coleccion, DesignColeccion

from server.serializers.DesignColeccionSerializer import DesignColeccionSerializer


class designColeccionViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    serializer_class = DesignColeccionSerializer

    def get_queryset (self):
        coleccion = self.request.query_params.get('coleccion', None)
        queryset = DesignColeccion.objects.all()
        if coleccion is not None:
            queryset = queryset.filter(coleccion=coleccion)
        return queryset


    @action(detail=True, methods=['post'])
    def set_image(self, request,):
        return Response('BAD REQUEST',
                        status=status.HTTP_400_BAD_REQUEST)
