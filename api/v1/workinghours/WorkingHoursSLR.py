# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import WorkingHours
from api.v1.workday.WorkDaySLR import WorkDaySerializer1

class WorkingHoursSerializer1(serializers.ModelSerializer):
    workday = WorkDaySerializer1(required = False, many=True)
    
    class Meta:
        model  = WorkingHours
        fields = [ 
            'workday',
        ]