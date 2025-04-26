from django.urls import path 
from .views import get_list_blog, detail_blog,  BlogMixinAPIViewPk, BlogGenericAPIView, BlogGenericAPIViewPk

urlpatterns = [
    path('', get_list_blog, name='blog-list'),
    path('<int:pk>/', detail_blog, name='blog-id'),
    path('bl/<int:pk>/', BlogMixinAPIViewPk.as_view()),
    path('blog/<int:pk>/',BlogGenericAPIViewPk.as_view()),
    path('blog/', BlogGenericAPIView.as_view())
]
