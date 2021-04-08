from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, ListView, DeleteView, CreateView

from webapp.models import Cart, Shop
from webapp.forms import CartAddForm, OrderForm


class CartAddView(CreateView):
    model = Cart
    form_class = CartAddForm

    def form_valid(self, form):
        qol = form.cleaned_data.get('qol', 1)
        self.shop = get_object_or_404(Shop, pk=self.kwargs.get('pk'))
        try:
            cart_shop = Cart.objects.get(shops=self.shop)
            cart_shop.qol += qol
            if cart_shop.qol <= self.shop.amount:
                cart_shop.save()
        except Cart.DoesNotExist:
            if qol <= self.shop.amount:
                Cart.objects.create(shops=self.shop, qol=qol)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return next
        return reverse('index')


class CartView(ListView):
    template_name = 'cart/view.html'
    context_object_name = 'shops'
    model = Cart
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = Cart.objects.all()
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm
        data = Cart.objects.all()
        total = 0
        for i in data:
            total += i.qol * i.shops.price
        context['total'] = total
        return context


class CartDeleteView(DeleteView):
    template_name = 'cart/view.html'
    model = Cart
    success_url = reverse_lazy('cart_view')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CartDeleteOneView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart_view')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.qty -= 1
        if self.object.qty < 1:
            self.object.delete()
        else:
            self.object.save()

        return HttpResponseRedirect(success_url)
