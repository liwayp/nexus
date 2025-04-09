from django.urls import path
from .views import contact_views

urlpatterns = [
    path('', contact_views, name='contact'),
]