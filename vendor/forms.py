from django import forms
from .models import Vendor
class VendorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Vendor
        fields = ('first_name','last_name','email_address','confirm_email','password','confirm_password')