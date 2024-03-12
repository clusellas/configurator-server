from rest_framework import serializers

from server.models import Valor


class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = ('id', 'code', 'description', 'image')
