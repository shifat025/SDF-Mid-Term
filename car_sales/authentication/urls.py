from django.urls import path
from . import views

urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('login/', views.Loginview.as_view(), name='Loginview'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password_change', views.pass_change, name='pass_change'),
    
]