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


class ProductInfoSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'price', 'product_type', 'description', 'source', 'name', 'views')
