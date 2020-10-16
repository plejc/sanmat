from rest_framework import serializers
from vendor.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('first_name','last_name','email_address','confirm_email','password','confirm_password')
    

 