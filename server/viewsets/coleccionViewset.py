from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from server.serializers import coleccionSerializer
from server.models import Coleccion
from guest_user.mixins import AllowGuestUserMixin


class coleccionViewset(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Coleccion.objects.all()
    serializer_class = coleccionSerializer.coleccionSerializer

    @action(detail=True, methods=['post'])
    def set_image(self, request, ):
        return Response('BAD REQUEST',
                        status=status.HTTP_400_BAD_REQUEST)

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
