from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(HistoryEntry)
admin.site.register(Cart)
admin.site.register(Store)
admin.site.register(Coupon)
