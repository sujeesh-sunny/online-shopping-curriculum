from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

