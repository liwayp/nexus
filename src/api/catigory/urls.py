from django.urls import path 
from .views import get_list_ctg, detail_ctg, DetailCategoryView, GetCategoryView

urlpatterns = [
    path('', get_list_ctg, name='catigory-list'),
    path('<int:pk>/', detail_ctg, name='detail-category'),
    path('testct/', GetCategoryView.as_view()),
    path('testct/<int:pk>/', DetailCategoryView.as_view())
]

