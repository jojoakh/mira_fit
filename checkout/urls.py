from django.urls import path
from .views import checkout, payment, payment_success

urlpatterns = [
    path('checkout/<int:plan_id>/', checkout, name='checkout'),
    path('payment/<int:order_id>/', payment, name='payment'),
    path('payment-success/<int:order_id>/',
         payment_success, name='payment_success'),
]
