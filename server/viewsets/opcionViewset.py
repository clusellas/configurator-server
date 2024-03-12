# Create your views here.
from rest_framework import viewsets
from server.models import Opcion
from server.serializers.opcionSerializer import OpcionFullSerializer


class opcionViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Opcion.objects.all()
    serializer_class = OpcionFullSerializer
