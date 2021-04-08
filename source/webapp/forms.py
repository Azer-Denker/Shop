from django import forms
from .models import CATEGORY_CHOICES, Shop, Order, Cart

default_status = CATEGORY_CHOICES[0][0]


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'category', 'amount', 'price']


class ShopDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название Проекта, чтобы удалить её')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class CartAddForm(forms.ModelForm):
    qol = forms.IntegerField(min_value=0, required=True, label="Количество",
                             widget=forms.NumberInput(attrs={'class': 'form-control  mt-3 mr-sm-2'}))

    class Meta:
        model = Cart
        fields = ['qol']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
