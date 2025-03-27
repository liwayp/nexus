from django.contrib import admin
from .models import Product, ProductImage, ProductView


admin.site.register(Product)
admin.site.register(ProductView)
admin.site.register(ProductImage)