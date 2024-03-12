from rest_framework import serializers
from server.models import Opcion
from server.serializers.valorSerializer import ValorSerializer


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('id', 'orden', 'name', 'valores')

class OpcionFullSerializer(serializers.ModelSerializer):
    valores = ValorSerializer(many=True)
    class Meta:
        model = Opcion
        fields = ('id', 'orden', 'name', 'valores')
