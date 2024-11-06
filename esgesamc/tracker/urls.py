# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate_emissions, name='calculate_emissions'),
    path('dashboard/', views.chartjs_chart , name='dashboard')
]
