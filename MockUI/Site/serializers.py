from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    EmailField,
    CharField,
    ValidationError,
    )

from .models import *
from django.contrib.auth import get_user_model
from django.db.models import Q


class CommentInfoSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'data', 'date_time')


class ProductInfoSerializer(ModelSerializer):

    comments = CommentInfoSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'price', 'product_type', 'description', 'source', 'name', 'views', 'comments')


class CartInfoSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'products')
