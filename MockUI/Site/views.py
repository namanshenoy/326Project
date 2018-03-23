from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, HistoryEntry, Cart, Store, Coupon  
from django.views import generic

# Create your views here.
def home(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)


class StoreView(generic.DetailView):
    """
    Generic class-based detail view for a store.
    """
    model = Store


class ClothingListView(generic.ListView):
    """
    Generic class-based list view for a list of clothing.
    """
    model = Product
    paginate_by = 10


class ClothingView(generic.DetailView):
    """
    Generic class-based detail view for a piece of clothing.
    """
    model = Product


class CartListView(generic.ListView):
    """
    Generic class-based detail view for a users cart.
    """
    model = Product
    paginate_by = 10 

    
class CouponListView(generic.ListView):
    """
    Generic class-based detail view for a list of coupons.
    """
    model = Coupon
    paginate_by = 10 


class CouponView(generic.DetailView):
    """
    Generic class-based detail view for a coupons.
    """
    model = Coupon