from rest_framework import serializers
from server.models import  DesignColeccion
from server.serializers.designSerializer import DesignSerializer


class DesignColeccionSerializer(serializers.ModelSerializer):

    design = DesignSerializer()
    class Meta:
        model = DesignColeccion
        fields = ('id', 'coleccion', 'design', 'img')
