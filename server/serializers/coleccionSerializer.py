from rest_framework import serializers
from server.models import Coleccion


class coleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coleccion
        fields = ('id','code', 'name', 'img')
