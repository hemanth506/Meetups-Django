from django.urls import path
from . import views

urlpatterns = [
    path('ecommerce/', views.e_index)
]