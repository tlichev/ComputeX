from django.urls import path
from .views import compute_view

urlpatterns = [
    path('compute/', compute_view, name='compute'),
]
