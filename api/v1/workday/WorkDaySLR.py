# Imports Python
# Imports Django
# Imports Django Library
from rest_framework import serializers

# Api
from api.models import WorkDay

class WorkDaySerializer1(serializers.ModelSerializer):
    day            = serializers.CharField(required = False)
    check_in_time  = serializers.TimeField(required = False)
    departure_time = serializers.TimeField(required = False)

    class Meta:
        model  = WorkDay
        fields = [ 
            'day',
            'check_in_time',
            'departure_time',
        ]