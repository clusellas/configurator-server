from rest_framework import serializers
from server.models import Design, Ancho, Eje, Coleccion, ConfigurationObject, Articles, ConfigurationOption
from server.serializers.articleSerializer import articleSerializer
from server.serializers.coleccionSerializer import coleccionSerializer
from server.serializers.configurationOptionSerializer import configurationOptionSerializer
from server.serializers.lineaConfiguradorSerializer import LineaConfiguradorSerializer


class configurationObjectSerializer(serializers.ModelSerializer):
    current_linea = LineaConfiguradorSerializer()
    articulo = articleSerializer()
    opciones_y_valores = serializers.SerializerMethodField()
    class Meta:
        model = ConfigurationObject
        fields = ('id', 'coleccion', 'design', 'ancho', 'eje', 'articulo','current_linea','opciones_y_valores')
        depth = 1
    def get_opciones_y_valores(self, obj):
        qset = ConfigurationOption.objects.filter(configuration_object=obj)
        return [configurationOptionSerializer(m).data for m in qset]


class CreateConfigurationObjectSerializer(serializers.ModelSerializer):
    coleccion_id = serializers.IntegerField()
    design_id = serializers.IntegerField()
    ancho_id = serializers.IntegerField()
    eje_id = serializers.IntegerField()

    class Meta:
        model = ConfigurationObject
        fields = ['coleccion_id', 'design_id', 'ancho_id', 'eje_id']
    def create(self, validated_data):
        # Retrieve the associated collection

        coleccion_id = validated_data.pop('coleccion_id')
        coleccion = Coleccion.objects.get(id=coleccion_id)
        validated_data['coleccion'] = coleccion

        design_id = validated_data.pop('design_id')
        design = Design.objects.get(id=design_id)
        validated_data['design'] = design

        ancho_id = validated_data.pop('ancho_id')
        ancho = Ancho.objects.get(id=ancho_id)
        validated_data['ancho'] = ancho

        eje_id = validated_data.pop('eje_id')
        eje = Eje.objects.get(id=eje_id)
        validated_data['eje'] = eje

        art = Articles.objects.get(coleccion=coleccion_id,ancho=ancho_id,design=design_id,eje=eje_id)
        validated_data['articulo'] = art

        current_linea = coleccion.lineaconfigurador_set.first()
        validated_data['current_linea'] = current_linea

        # Create and return the configuration object
        return ConfigurationObject.objects.create(**validated_data)