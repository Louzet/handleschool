"""
    handleschool URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.get_accounts),
    path('accounts/create', views.post_accounts),
]
