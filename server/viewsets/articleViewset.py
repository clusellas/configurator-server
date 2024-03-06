from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from server.models import Articles, Ancho
from server.serializers.articleSerializer import articleSerializer, designArticleSerializer, anchoArticleSerializer, \
    ejeArticleSerializer ,coleccionArticleSerializer


class articleViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Articles.objects.all()
    serializer_class = articleSerializer
    backend_filter_fields = ['CodigoFamilia', 'CodigoSubfamilia', 'coleccion', 'design', 'ancho', 'eje', 'visible']


    def get_serializer_class(self):
        show_coleccion = self.request.query_params.get('show_coleccion', None)
        show_design = self.request.query_params.get('show_design', None)
        show_ancho = self.request.query_params.get('show_ancho', None)
        show_eje = self.request.query_params.get('show_eje', None)

        if show_coleccion is not None and show_coleccion == 'true':
            return coleccionArticleSerializer
        elif show_design is not None and show_design == 'true':
            return designArticleSerializer
        elif show_ancho is not None and show_ancho == 'true':
            return anchoArticleSerializer
        elif show_eje is not None and show_eje == 'true':
            return ejeArticleSerializer

        return articleSerializer

    def get_queryset(self):
        for key, value in self.request.query_params.items():
            if key in self.backend_filter_fields:

                # if key == 'ancho':
                #     valor_ancho = Ancho.objects.filter(code__gte=value).order_by('code').first()
                #     self.queryset = self.queryset.filter(ancho=valor_ancho)

                self.queryset = self.queryset.filter(**{key: value})

        show_coleccion = self.request.query_params.get('show_coleccion', None)
        show_design = self.request.query_params.get('show_design', None)
        show_ancho = self.request.query_params.get('show_ancho', None)
        show_eje = self.request.query_params.get('show_eje', None)

        if show_coleccion is not None and show_coleccion == 'true':
            self.queryset = self.queryset.distinct('coleccion')
        elif show_design is not None and show_design == 'true':
            self.queryset = self.queryset.distinct('design')
        elif show_ancho is not None and show_ancho == 'true':
            self.queryset = self.queryset.distinct('ancho')
        elif show_eje is not None and show_eje == 'true':
            self.queryset = self.queryset.distinct('eje')

        return self.queryset