from django.urls import path
from .views import (
    difference,
    triplet,
)

urlpatterns = [
    path('difference/', difference, name='difference'),
    path('triplet/', triplet, name='triplet'),
]