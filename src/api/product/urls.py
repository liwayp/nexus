from django.urls import path 
from .views import get_list_pr, get_product


urlpatterns = [
    path('', get_list_pr, name='product-list'),
    path('<int:pk>/', get_product , name='product-id')
]
