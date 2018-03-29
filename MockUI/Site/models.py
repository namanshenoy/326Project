from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    date_time = models.DateTimeField()
    products = models.ManyToManyField('Product', blank=True, related_name="%(app_label)s_%(class)s_products")

    def __str__(self):
        return str(self.date_time)


class Coupon(models.Model):
    code = models.CharField(max_length=64)
    description = models.TextField()
    coupon_type = models.CharField(max_length=64)
    discount = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.description


class HistoryEntry(models.Model):
    date_time = models.DateTimeField()
    product = models.ForeignKey('Product', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        verbose_name = 'History Entry'
        verbose_name_plural = 'History Entries'


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    product_type = models.CharField(max_length=64)
    description = models.TextField()
    source = models.CharField(max_length=200)
    name = models.TextField()
    views = models.IntegerField()
    size_type = models.CharField(max_length=64, blank=True, null=True)
    size_primary = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    size_secondary = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    images = models.ManyToManyField('Image', blank=True, related_name="%(app_label)s_%(class)s_images")

    def __str__(self):
        return self.name


class Image(models.Model):
    source = models.URLField(null=True)


class Store(models.Model):
    store_url = models.CharField(max_length=200)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    products = models.ForeignKey('Product', blank=True, null=True, on_delete=models.CASCADE)
    coupons = models.ForeignKey('Coupon', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    history = models.ManyToManyField('HistoryEntry', blank=True, related_name="%(app_label)s_%(class)s_history")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'User Information'
        verbose_name_plural = 'User Information'
