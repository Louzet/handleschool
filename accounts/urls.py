"""
    handleschool URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_accounts),
    path('create', views.post_accounts),
]
