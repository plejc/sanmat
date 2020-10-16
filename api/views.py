from django.shortcuts import render
from rest_framework import generics
from vendor.models import Vendor
from .serializers import VendorSerializer


class VendorAPIView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
