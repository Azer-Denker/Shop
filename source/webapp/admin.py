from django.contrib import admin
from webapp.models import Shop, Order, OrderShop


class ShopAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'created_at']
    list_filter = ['created_at']


class OrderShopAdmin(admin.ModelAdmin):
    list_display = ['shop', 'qol']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderShop, OrderShopAdmin)
