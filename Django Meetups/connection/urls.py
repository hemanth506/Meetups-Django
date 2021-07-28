from django.urls import path
from . import views
from meetups.urls import urlpatterns as meetupsUrls
from ecommerce.urls import urlpatterns as ecommerceUrls

urlpatterns = [
    path('', views.connect),
]