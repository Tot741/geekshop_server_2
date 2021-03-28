
from django.contrib import admin

from ordersapp.models import Order, OrderItem


admin.site.register(Order)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    fields = ('order', 'product', 'quantity')
    readonly_fields = ('order', 'product')
    ordering = ('order',)
    list_filter = ('order',)