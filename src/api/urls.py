from django.urls import path, include


urlpatterns = [
    path('catigory/', include('api.catigory.urls')),
    path('region/', include('api.region.urls')),
    path('product/', include('api.product.urls')),
    path('blog/', include('api.blog.urls')),
]
