from rest_framework import serializers
from server.models import Eje


class ejeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eje
        fields = ('id', 'code', 'name', 'image')
