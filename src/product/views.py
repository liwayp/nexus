from django.shortcuts import render
from .models import Product
from catigory.models import *
from product.models import *
from django.db.models import Prefetch
from django.core.paginator import Paginator
from .models import *
from  user.models import User
from django.shortcuts import redirect
from django.db.models import Count




def product_list(request):
    page = request.GET.get('page', 1)
    categories = Category.objects.filter(is_main=True)
    categories_count = Category.objects.annotate(product_count=Count('product')).filter(product_count__gt=0)
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
        'count': paginator.count,
        "categories_count": categories_count,
    }
    return render(request, 'products.html', ctx)



def product_detail(request, pk):
    # product = Product.objects.get(pk=pk)
    product = Product.objects.prefetch_related('images').get(pk=pk)
    # image = ProductImage.objects.get(image=True)
    # image = ProductImage.objects.filter(product=product.id)
    # location = Product.objects.filter(Product.location)
    description = Product.objects.filter(location = True)
    
    
    
    ctx = {
        "product":product,
        # "image":image,
        "description":description,
        # "location":location,
    }
    return render(request, 'detail.html', ctx)



def product_add(request):
    if request.method == "POST":
        form = Profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = Profile()  

        
    return render(request, 'products_add.html', {'form': form})  



