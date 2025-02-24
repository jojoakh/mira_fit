from django.urls import path
from .views import checkout

urlpatterns = [
    path('<int:plan_id>/', checkout, name='checkout'),
]
