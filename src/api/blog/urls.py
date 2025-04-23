from django.urls import path 
from .views import get_list_blog, detail_blog

urlpatterns = [
    path('', get_list_blog, name='blog-list'),
    path('<int:pk>/', detail_blog, name='blog-id')
]

