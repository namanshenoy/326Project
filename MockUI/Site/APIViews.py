# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .serializers import *

from django.contrib.auth import get_user_model
from .models import *

class UpdateCart(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartInfoSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            if not UserInfo.objects.get(id=request.user.id).cart.id == int(kwargs['id']):
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            return super(UpdateCart, self).update(request, *args, **kwargs)

class ProductByNameAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductInfoSerializer

    #def get_queryset(self):
    #    return Order.objects.filter(user=self.request.user, status='Open')

    def filter_queryset(self, queryset):
        queryset = super(ProductInfoAPIView, self).filter_queryset(queryset)
        return queryset.order_by('name')
