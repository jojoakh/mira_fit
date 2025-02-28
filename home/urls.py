from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.client_reviews, name='client_reviews'),
]
