from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, HistoryEntry, Cart, Store, Coupon, UserInfo
from django.views import generic
from django.contrib.auth import authenticate, login
import json

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
    template_name = 'cart.html'
    model = Cart
    paginate_by = 10

def cart(request):
    cart = UserInfo.objects.get(user=int(request.user.id)).cart
    print(cart.products.all())
    return render(request, 'cart.html', context={'cart':cart})


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


class HistoryListView(generic.ListView):
    model = HistoryEntry


class UserDetailView(generic.DetailView):
    model = UserInfo
    template_name = 'user_detail.html'
    context_object_name = 'userinfo'

    def get_object(self):
        userinfo = get_object_or_404(UserInfo, user=self.request.user)
        print(userinfo.history)
        return userinfo


def AjaxLogin(request):
    if request.POST:
        print(request.POST)
        data = json.loads(list(request.POST)[0])
        username= data['username']
        password = data['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('fine')
            else:
                return HttpResponse('inactive')
        else:
            return HttpResponse('bad')
    else:
        return HttpResponse('bad')