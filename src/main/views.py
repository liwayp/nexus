from django.shortcuts import render
from catigory.models import *
from product.models import *
from django.db.models import Prefetch


# def index(request):
#     is_main = Category.objects.filter(is_main=True)
#     context = {'categories':is_main}
    
#     return render(request, 'index.html',context)

def index(request):
    categories = Category.objects.filter(is_main=True)
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    
    ctx = {
        "categories": categories,
        "products": products
    }
    return render(request, 'index.html', ctx)


def add_products (request):
    pass 


    ctx = {

    }

    return render(request, 'products_add',)

