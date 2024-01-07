from django.urls import path
from . import views

urlpatterns = [
    path('profile/add_brand', views.add_brand, name='add_brand'),  
]




