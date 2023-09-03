from . import views
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', views.get_clientes, name='get_all_users'), 
    path('user/<str:nick>', views.get_pelo_username),  
    path('data/', views.geren_cliente)
]