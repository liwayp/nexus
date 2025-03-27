from django.urls import path
from .views import index
from user.views import login_view,logout_view,register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='main'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register, name='register'),
    
]






