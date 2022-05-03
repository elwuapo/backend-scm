# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import Mark
from api.v1.browser.BrowserSLR import BrowserSerializer1
from api.v1.employee.EmployeeSLR import EmployeeSerializer1

class MarkSerializer1(serializers.ModelSerializer):
    employee       = EmployeeSerializer1(required = False)
    place          = serializers.CharField(required = False)
    check_in_time  = serializers.DateTimeField(required = False)
    departure_time = serializers.DateTimeField(required = False)
    browser        = BrowserSerializer1(required = False)

    class Meta:
        model  = Mark
        fields = [
            'pk',
            'employee',
            'place',
            'check_in_time',
            'departure_time',
            'browser',
        ]