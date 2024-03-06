from rest_framework import serializers
from server.models import  DesignColeccion


class DesignColeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignColeccion
        fields = ('id', 'coleccion', 'design', 'img')
