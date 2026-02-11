from django.contrib import admin
from .models import Product, Category, Cart, Order, Payment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)