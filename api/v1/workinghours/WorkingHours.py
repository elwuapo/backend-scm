# Imports Python
from datetime import datetime, timedelta, time

# Imports Django
from django.utils import timezone

# Imports Django Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Api
from api.models import Account, Mark


class WorkingHoursAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            """
            user           = request.user
            account        = Account.objects.get(user = user)
            working_hours  = account.working_hours

            date_joined    = user.date_joined.date()
            since_the_date = datetime.now().date() 
            till_the_date  = datetime.now().date() + timedelta(days=1)

            today = datetime.today().strftime('%A').lower()
            
            exist_workday = working_hours.workday.filter(day = today).exists()

            if(exist_workday):
                workday = working_hours.workday.filter(day = today).first()

                exist_mark = Mark.objects.filter(employee = user, check_in_time__range=(since_the_date, till_the_date)).exists()

                if(exist_mark):
                    mark = Mark.objects.filter(employee = user, check_in_time__range=(since_the_date, till_the_date)).first()

                    time1 = workday.check_in_time
                    time2 = time(mark.check_in_time.hour, mark.check_in_time.minute, mark.check_in_time.second)
                    
                    return Response({'late': time1 < time2}, status=200)
                else:
                    time1 = workday.check_in_time
                    time2 = time(datetime.today().hour, datetime.today().minute, datetime.today().second)

                    if(time1 < time2):
                        Response({'type': 'correcto'}, status=200)
                    else:
                        Response({'type': 'atraso'}, status=200)

                    Response({'type': 1}, status=200)
            """
            return Response(status=200)
        except:
            return Response(status=400)

    def post(self, request):
        try:
            return Response(status=200)
        except:
            return Response(status=400)

    def put(self, request, pk):
        try:
            return Response(status=200)
        except:
            return Response(status=400)

    def delete(self, request, pk):
        try:
            return Response(status=200)
        except:
            return Response(status=400)