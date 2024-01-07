from django.urls import path
from . import views



urlpatterns = [
    path('profile/add_car/', views.add_car, name='add_car'),  
     path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
     path('buy/<int:id>/', views.buynow, name='buynow'),
]

