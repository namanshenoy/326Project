from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, HistoryEntry, Cart, Store, Coupon
from django.views import generic

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def user(request):
    return render(request, 'user_detail.html', {})


def contact(request):
    return render(request, 'contact.html', {})

class StoreView(generic.DetailView):
    """
    Generic class-based detail view for a store.
    """
    model = Store


class ClothingListView(generic.ListView):
    """
    Generic class-based list view for a list of clothing.
    """
    template_name = 'home.html'
    model = Product
    paginate_by = 10


class ClothingView(generic.DetailView):
    """
    Generic class-based detail view for a piece of clothing.
    """
    model = Product
    pk_url_kwarg = "product_id"
    template_name = "item_detail.html"


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
