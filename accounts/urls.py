"""
    handleschool URL Configuration
"""
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.get_accounts),
    path('create', views.post_accounts),
]
