from django.db import models
from django.contrib.auth import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User)
    

class Product(models.Model):
    price = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2, default=0)
    type = models.CharField(max_length=64, blank=False, null=False, default="Pants")
    description = models.TextField(blank=False, null=False, default="No description")
    # images = models.URLField()
    source = models.URLField(blank=False, null=False, default="http://google.com/")
    name = models.TextField(blank=False, null=False, default='Unnamed Product')  
    # notice me senpai
    
    
"""Carts Model



Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension
"""
class Cart(models.Model):
    products = models.ManyToManyField('Product', blank=True, related_name="%(app_label)s_%(class)s_products")
    
class User(models.Model):
    name = models.CharField(max_length=15)
    cart = models.ForeignKey(Cart)
    history = models.ManyToManyField('Product', blank=True, related_name="%(app_label)s_%(class)s_products")

class Store(models.Model):
    products = models.ManyToManyField('Product', blank=True)