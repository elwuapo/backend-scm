# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import Account
from api.v1.employee.EmployeeSLR import EmployeeSerializer1
from api.v1.workinghours.WorkingHoursSLR import WorkingHoursSerializer1
from api.v1.mark.MarkSLR import MarkSerializer1

class AccountSerializer1(serializers.ModelSerializer):
    user          = EmployeeSerializer1(required = False)
    avatar        = serializers.ImageField(required = False)
    role          = serializers.CharField(required = False)
    working_hours = WorkingHoursSerializer1(required = False)
    
    class Meta:
        model  = Account
        fields = [ 
            'user',
            'avatar',
            'role',
            'working_hours',
        ]