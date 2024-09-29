from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
   

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')
