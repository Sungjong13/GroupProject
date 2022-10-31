from django.shortcuts import render
from store.models import Product

def main_page(request):
    return render(request, 'main.html')

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)

