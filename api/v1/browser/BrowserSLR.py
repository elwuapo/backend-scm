# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import Browser

class BrowserSerializer1(serializers.ModelSerializer):
    id   = serializers.CharField(required = False)
    name = serializers.CharField(required = False)
    os   = serializers.CharField(required = False)
    
    class Meta:
        model  = Browser
        fields = [
            'id',
            'name',
            'os',
        ]