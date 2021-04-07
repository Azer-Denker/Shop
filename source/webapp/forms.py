from django import forms
from .models import CATEGORY_CHOICES, Shop

default_status = CATEGORY_CHOICES[0][0]


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'category', 'amount', 'price']


class ShopDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название Проекта, чтобы удалить её')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
