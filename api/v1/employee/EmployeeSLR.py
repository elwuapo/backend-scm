# Imports Python
# Imports Django
from django.contrib.auth.models import User

# Imports Django Library
from rest_framework import serializers

# Api



class EmployeeSerializer1(serializers.ModelSerializer):
    username   = serializers.CharField(required = False)
    first_name = serializers.CharField(required = False)
    last_name = serializers.CharField(required = False)
    email      = serializers.EmailField(required = False)
    
    class Meta:
        model  = User
        fields = [ 
            'username', 
            'first_name', 
            'last_name', 
            'email',
        ]