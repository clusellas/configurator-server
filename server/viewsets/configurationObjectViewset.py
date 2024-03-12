from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from server.serializers import configurationObjectSerializer
from server.models import ConfigurationObject, Opcion, Valor


class configurationObjectViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = ConfigurationObject.objects.all()

    serializer_class = configurationObjectSerializer.configurationObjectSerializer
    create_serializer_class = configurationObjectSerializer.CreateConfigurationObjectSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return self.create_serializer_class
        return self.serializer_class

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer.instance.fill_from_linea()
        return Response({'id': serializer.instance.pk}, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def set_value_option(self, request, pk):
        option_id = request.data.get('optionId')
        value_id = request.data.get('valueId')
        option = Opcion.objects.get(id=option_id)
        value = Valor.objects.get(id=value_id)

        self.get_object().update_option_value(option, value)

        return Response({'message': 'Custom action performed successfully'}, status=status.HTTP_200_OK)

# @action(detail=False)
# def recent_users(self, request):
#     recent_users = User.objects.all().order_by('-last_login')
#
#     page = self.paginate_queryset(recent_users)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     serializer = self.get_serializer(recent_users, many=True)
#     return Response(serializer.dat
