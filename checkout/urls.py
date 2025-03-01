from django.urls import path
from .views import checkout, payment_success

urlpatterns = [
    path('checkout/<int:plan_id>/', checkout, name='checkout'),
    path('payment-success/<int:order_id>/',
         payment_success, name='payment_success'),
]
