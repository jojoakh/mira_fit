from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:plan_id>/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('payment-success/<int:order_id>/',
         views.payment_success, name='order_success'),
]
