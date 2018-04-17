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
from django.contrib.auth.models import User


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class CommentInfoSerializer(ModelSerializer):
    user = UserInfoSerializer(read_only=True, many=False)
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
