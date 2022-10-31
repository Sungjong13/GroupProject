from django.urls.conf import include
from category.models import Category
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
      products = Product.objects.all().filter(is_available=True)
      products_count = products.count()
    context = {
      'products': products,
      'products_count': products_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
      'single_product': single_product,
      'in_cart': in_cart,
    }

    return render(request, 'store/product_detail.html', context)
  
