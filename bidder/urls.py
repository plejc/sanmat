from django.urls import path
from .import views


urlpatterns = [
    path('home/',views.home, name ='home'),
    path('book/',views.book, name ='book'),
    path('bidder/',views.bidder, name ='bidder'),
]