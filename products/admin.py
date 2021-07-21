from django.contrib import admin

from products.models import ProductsCategory, Products, Basket


admin.site.register(ProductsCategory)
admin.site.register(Products)
admin.site.register(Basket)
