# myapp/urls.py

from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.index, name='index'),  
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),  
    
]
