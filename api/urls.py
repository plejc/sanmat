from django.urls import path
from .views import VendorAPIView



urlpatterns = [
    path('',VendorAPIView.as_view()),
]