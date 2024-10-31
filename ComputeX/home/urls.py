from django.contrib import admin
from django.urls import path

from ComputeX.home.views import show_index

urlpatterns = [
    path('', show_index, name='home'),

]