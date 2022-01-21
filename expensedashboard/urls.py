
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('billing/', views.billing, name = 'billing'),
    path('sub-expense/', views.subexpense, name = 'sub-expense'),
    path('notifications/', views.notifications, name = 'notifications'),
    path('profile/', views.profile, name = 'profile'),
    
]
