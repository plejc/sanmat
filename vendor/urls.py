from django.urls import path
from .views import VendorListView
from .import views


urlpatterns = [
    path('',VendorListView.as_view(),name='home'),
    path('home/',views.home, name='home'),
    path('home/vendor/',views.vendor_view, name = 'vendor_view'),
    path('book/',views.book, name = 'book'),
]