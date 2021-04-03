from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.core.cache import cache

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None):
#     context = {
#         'title': 'geekshop - каталог',
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'mainapp/products.html', context)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all().order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.all().order_by('price')


def get_products_in_category(category_id):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{category_id}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=category_id)
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category_id=category_id)


def products(request, category_id=None, page=1):
    products = get_products_in_category(category_id) if category_id else Product.get_all()
    per_page = 3
    paginator = Paginator(get_products_orederd_by_price(), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'geekshop - каталог',
        'products': products_paginator,
        'categories': ProductCategory.get_all(),
    }
    return render(request, 'mainapp/products.html', context)
