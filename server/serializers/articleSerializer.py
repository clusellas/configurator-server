from rest_framework import serializers
from server.models import Articles
from server.serializers.DesignColeccionSerializer import DesignColeccionSerializer
from server.serializers.anchoSerializer import anchoSerializer
from server.serializers.coleccionSerializer import coleccionSerializer
from server.serializers.ejeSerializer import ejeSerializer


class articleSerializer(serializers.ModelSerializer):
    coleccion = coleccionSerializer(many=False, read_only=True)
    # designs = designSerializer(many=False, read_only=True)
    design_coleccion = DesignColeccionSerializer(many=False, read_only=True)
    ancho = anchoSerializer(many=False, read_only=True)
    eje = ejeSerializer(many=False, read_only=True)

    class Meta:
        model = Articles
        fields = [
        'id', 'CodigoEmpresa', 'CodigoArticulo', 'DescripcionArticulo', 'CodigoFamilia', 'CodigoSubfamilia', 'ancho',
        'eje', 'coleccion', 'design','design_coleccion', 'visible']


class coleccionArticleSerializer(serializers.ModelSerializer):
    coleccion = coleccionSerializer(many=False, read_only=True)

    class Meta:
        model = Articles
        fields = ['coleccion']

class designArticleSerializer(serializers.ModelSerializer):
    design_coleccion = DesignColeccionSerializer(many=False, read_only=True)

    class Meta:
        model = Articles
        fields = ['design_coleccion']
class anchoArticleSerializer(serializers.ModelSerializer):
    ancho = anchoSerializer(many=False, read_only=True)

    class Meta:
        model = Articles
        fields = ['ancho']

class ejeArticleSerializer(serializers.ModelSerializer):
    eje = ejeSerializer(many=False, read_only=True)

    class Meta:
        model = Articles
        fields = ['eje']
