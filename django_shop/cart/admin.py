from django.contrib import admin
from .models import OrderItem, Order


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('profile', 'order_name', 'order_email', 'order_phone', 'order_address', 'created')
    list_filter = ('ordered', 'created')


