from rest_framework import serializers
from server.models import Opcion


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('id', 'orden', 'name', 'valores')
