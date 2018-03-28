from django.core.management.base import BaseCommand
from Site.models import *

class Command(BaseCommand):
    def handle(self, **options):
        # now do the things that you want with your models here
        for i in range(1, 100):
            product = Product(price=32, product_type='pants', description='hey', source='http://google.com', name='banana', views=32)
            product.save()
