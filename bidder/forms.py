from django import forms
from .models import Bidder
class BidderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Bidder
        fields = ('first_name','last_name','email_address','confirm_email','password','confirm_password')