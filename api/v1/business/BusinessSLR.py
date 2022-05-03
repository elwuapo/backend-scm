# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import Business
from api.v1.account.AccountSLR import AccountSerializer1

class BusinessSerializer1(serializers.ModelSerializer):
    name            = serializers.CharField(required = False)
    employees       = AccountSerializer1(required = False, many=True)
    external_system = serializers.BooleanField(required= False)
    redirect_to     = serializers.CharField(required = False)
    us              = serializers.CharField(required = False)
    image           = serializers.ImageField(required = False)

    class Meta:
        model  = Business
        fields = [
            'pk',
            'name',
            'employees',
            'external_system',
            'redirect_to',
            'us',
            'image'
        ]