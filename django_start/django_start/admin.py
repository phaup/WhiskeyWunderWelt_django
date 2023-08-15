#admin.py

from django.contrib import admin
from .models import Product, Order, Review

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)