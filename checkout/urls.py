from django.urls import path
from .views import checkout, payment_success

urlpatterns = [
    path('checkout/<int:plan_id>/', checkout, name='checkout'),
    path('success/<str:payment_intent_id>/',
         payment_success, name='payment_success'),
]
