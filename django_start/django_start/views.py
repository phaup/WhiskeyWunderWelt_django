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

def start_page(request):
    return render(request, 'django_start/start_page.html')

def privacy_policy(request):
    return render(request, 'django_start/privacy_policy.html')

def imprint(request):
    return render(request, 'django_start/imprint.html')

def start_page(request):
    products = Product.objects.all()
    return render(request, 'django_start/start_page.html', {'products': products})