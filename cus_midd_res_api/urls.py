from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
  #  path('', include(router.urls)),
  #  path('api-auth/', include('rest_framework.urls')),
  #  path('contect/', ContactView.as_view(),name='contact'),
   path('jobapply/',JobApplyView.as_view(),name='jobapply'),
]

