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

class ProductByNameAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductInfoSerializer

    #def get_queryset(self):
    #    return Order.objects.filter(user=self.request.user, status='Open')

    def filter_queryset(self, queryset):
        queryset = super(ProductInfoAPIView, self).filter_queryset(queryset)
        return queryset.order_by('name')
