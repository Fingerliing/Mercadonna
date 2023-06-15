from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    
    categories = Category.objects.all()

    CATID = request.GET.get('categories')
    
    if CATID:
        products = Product.objects.filter(category_id=CATID)
    else:
        products = Product.objects.all()
        
    context = {
        'products':products,
        'categories':categories,
        }
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html')

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html')

