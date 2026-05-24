# produtos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaprodutos, name='listaprodutos'),
]