from django.urls import path 
from .views import get_list_regions, detail_region

urlpatterns = [
    path('', get_list_regions, name='region-list'),
    path('product/<int:pk>/', detail_region, name='region-id')
]

