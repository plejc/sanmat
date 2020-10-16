from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from .models import Vendor
from .forms import VendorForm

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor_list.html'

def home(request):
    return render(request,'vendor/home.html')
def book(request):
    return render(request,'vendor/book.html')


def vendor_view(request):
    
    if request.method == 'POST':
        form = VendorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = VendorForm()
    return render(request,'vendor/vendor.html',{'form':form})
