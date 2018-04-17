# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

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

class addCommentToProduct(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = CommentInfoSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        data = request.data
        #serializer = self.get_serializer(data=data)
        product = get_object_or_404(Product, id=int(kwargs['id']))
        comment = Comment(user=request.user, data=data['data'])
        comment.save()
        product.comments.add(comment)
        product.save()
        return Response(status=HTTP_201_CREATED)
        #return super(addCommentToProduct, self).update(request, *args, **kwargs)

class CommentsFromProduct(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentInfoSerializer

    def get_queryset(self):
        product = get_object_or_404(Product, id=int(self.kwargs['product_id']))
        return product.comments

class UpdateCart(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartInfoSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            if not UserInfo.objects.get(user=request.user.id).cart.id == int(kwargs['id']):
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            return super(UpdateCart, self).update(request, *args, **kwargs)

class AddToCart(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartInfoSerializer

    def get_object(self):
        return UserInfo.objects.get(user=request.user.id).cart

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        cart_products = UserInfo.objects.get(user=request.user.id).cart.products
        cart_products.add(Product.objects.get(id=int(data['products'][0])))
        if serializer.is_valid():
            return Response(serializer.errors, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RemoveFromCart(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartInfoSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        cart_products = UserInfo.objects.get(user=request.user.id).cart.products
        for product in data['products']:
            cart_products.remove(Product.objects.get(id=int(product)))
        #cart_products.remove(Product.objects.get(id=int(data['products'][0])))
        if serializer.is_valid():
            return Response(serializer.errors, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ProductByNameAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductInfoSerializer

    #def get_queryset(self):
    #    return Order.objects.filter(user=self.request.user, status='Open')

    def filter_queryset(self, queryset):
        queryset = super(ProductInfoAPIView, self).filter_queryset(queryset)
        return queryset.order_by('name')

class ItemInCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = request.data
        productId = self.kwargs.get('product_id')
        cart_products = UserInfo.objects.get(user=request.user.id).cart.products
        print(cart_products.filter(id=productId))
        print('Product Id = ', productId)
        if cart_products.filter(id=productId).exists():
            return Response(data={'inCart':True})
        else:
            return Response(data={'inCart':False})
