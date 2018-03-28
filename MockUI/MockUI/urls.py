"""MockUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import Site.views as site_views
from Site import APIViews
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView

from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', site_views.ClothingListView.as_view(), name='HomeView'),
    url(r'^product/(?P<product_id>\d+)$', site_views.ClothingView.as_view(), name='ProductDetailView'),
    # url(r'^cart/$', site_views.cart, name='cart'),
    url(r'^cart/$', site_views.CartListView.as_view(), name='CartView'),
    url(r'^cart/add/$', APIViews.AddToCart.as_view(), name='AddToCart'),
    url(r'^cart/remove/$', APIViews.RemoveFromCart.as_view(), name='RemoveFromCart'),
    url(r'^products/$', APIViews.ProductByNameAPIView.as_view(), name='ProductByNameAPI'),
    url(r'^checkItem/(?P<product_id>\d+)$', APIViews.ItemInCartAPIView.as_view(), name='CjeckItemAPI'),
    url(r'^user/$', site_views.user, name='user'),
    url(r'^contact/$', site_views.contact, name='contact'),
    path('', RedirectView.as_view(url='/home/')),
]
