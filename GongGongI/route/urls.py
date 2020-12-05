from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index),

    path('map/', views.map),
    path('navbar/', views.navbar),


]
