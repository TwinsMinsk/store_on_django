from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, ProductsCategory, Basket
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page=1):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductsCategory.objects.all(),
    }
    if category_id:
        products = Products.objects.filter(category_id=category_id)
    else:
        products = Products.objects.all()

    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)

@login_required
def basket_add (request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_delete(request,id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


