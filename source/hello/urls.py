"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('shop/<int:pk>/', ShopView.as_view(), name='shop_view'),
    path('shops/add/', ShopCreateView.as_view(), name='shop_create'),
    path('shop/<int:pk>/update/', ShopUpdateView.as_view(), name='shop_update'),
    path('shop/<int:pk>/delete/', ShopDeleteView.as_view(), name='shop_delete'),
    path('shop/<int:pk>/cart/add/', CartAddView.as_view(), name='cart_add'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),
    path('order/', OrderCreateView.as_view(), name='order_create'),
]
