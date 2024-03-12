from rest_framework import serializers
from server.models import Design


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = ('id', 'code', 'name')
