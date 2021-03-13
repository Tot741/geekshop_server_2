from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

def products(request, category_id=None, page=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'geekshop - каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
