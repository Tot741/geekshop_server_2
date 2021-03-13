from django.contrib import admin
from mainapp.models import ProductCategory, Product
# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'category', ('price', 'quantity'), 'description', 'short_description')
    # readonly_fields = ('price', 'quantity')
    ordering = ('name',)
    search_fields = ('name', 'category__name')
