from rest_framework import serializers
from server.models import ConfigurationOption, Valor, Opcion


class configurationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationOption
        fields = ('id', 'valor', 'opcion')