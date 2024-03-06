from rest_framework import serializers
from server.models import Ancho


class anchoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ancho
        fields = ('id', 'code', 'name')

