# views.py

from django.shortcuts import render
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'django_start/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'django_start/product_detail.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'django_start/order_list.html', {'orders': orders})
