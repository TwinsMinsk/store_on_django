from django.db import models

# Create your models here.
from django.db.models import CASCADE

from users.models import User


class ProductsCategory(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product categories'


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    images = models.ImageField(upload_to='products_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductsCategory, on_delete=CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

    class Meta:
        verbose_name_plural = 'Products'


class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price