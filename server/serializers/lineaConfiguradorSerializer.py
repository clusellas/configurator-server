from rest_framework import serializers

from server.models import LineaConfigurador
from server.serializers.opcionSerializer import OpcionSerializer


class LineaConfiguradorSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True)
    class Meta:
        model = LineaConfigurador
        fields = ('price', 'standard', 'coleccion', 'opciones')