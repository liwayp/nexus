from django.urls import path
from .views import region
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', region, name='region')
]

