from django.shortcuts import redirect
from django.views.generic import CreateView

from webapp.forms import OrderForm
from webapp.models import Shop, Order, Cart, OrderShop


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        order = Order.objects.create(name=name, phone=phone, address=address)
        cart = Cart.objects.all()
        for i in cart:
            shop = Shop.objects.get(pk=i.shops.pk)
            OrderShop.objects.create(shop=i.shops,
                                     order=order,
                                     qol=i.qol)
            shop.amount = shop.amount-i.qol
            shop.save()
        cart.delete()
        return redirect('index')


