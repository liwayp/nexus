from django.shortcuts import render
from .models import Product
from catigory.models import *
from product.models import *
from django.db.models import Prefetch
from django.core.paginator import Paginator
from .models import *



def product_list(request):
    page = request.GET.get('page', 1)
    categories = Category.objects.filter(is_main=True)
    region = Region.objects.all()
    
    products =  Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)

    ctx = {
        "categories": categories,
        "region": region,
        "products": products,
        "paginator": paginator,
        "page_obj": page_obj,
        'count': paginator.count
    }
    return render(request, 'products.html', ctx)



def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    # image = ProductImage.objects.get(image=True)
    image = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
     
    
    ctx = {
        "product":product,
        "image":image,
        
    }
    return render(request, 'detail.html', ctx)
