from django.urls import path
from django import views
from .import views
from .views import *

urlpatterns = [
    
    path('indexdate/',views.index),
]
