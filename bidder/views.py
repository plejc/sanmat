from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from .models import Bidder

from .forms import BidderForm


def home(request):
    return render(request,'bidder/home.html')
def book(request):
    return render(request,'bidder/book.html')


def bidder(request):
    
    if request.method == 'POST':
        form = BidderForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BidderForm()
    return render(request,'bidder/bidder.html',{'form':form})
