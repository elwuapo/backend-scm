# Imports Python
import os
from io import BytesIO
from datetime import datetime

# Imports Django
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone

# Imports Django Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Api
from api.utils import encode_photo, match
from api.models import Account, Browser, Business, Mark
from api.v1.mark.MarkSLR import MarkSerializer1
from api.v1.employee.EmployeeSLR import EmployeeSerializer1
from api.v1.account.AccountSLR import AccountSerializer1

from backend.settings import BASE_DIR

class MarkAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, option):
        try:
            user = request.user
            account = Account.objects.get(user = user)

            if(option == 'marking'):
                today = datetime.now().date()
                exist_mark = account.marks.filter(check_in_time__date = today).exists()
                serializer1 = EmployeeSerializer1(user)

                if(exist_mark):
                    mark = account.marks.filter(check_in_time__date = datetime.now().date()).first()
                    serializer2 = MarkSerializer1(mark)
                    return Response({'mark': serializer2.data}, status=200)
                else:
                    return Response({'mark': {'employee' : None, 'place': None, 'check_in_time': None, 'departure_time': None}}, status=200)
            elif(option == 'schedule'):
                marks   = account.marks.all()[:5]
                
                serializer1 = AccountSerializer1(account)
                serializer2 = MarkSerializer1(marks, many=True)
                
                return Response({"account": serializer1.data, "marks": serializer2.data},status=200)
            elif(option == 'attendance'):
                business   = Business.objects.filter(employees__pk = account.pk).first()
                marks      = business.marks.all()
                serializer = MarkSerializer1(marks, many=True)

                return Response({'marks': serializer.data}, status=200)
            else:
                return Response(status=400)
        except:
            return Response(status=400)

    def post(self, request):
        try:
            data  = request.data
            user  = request.user
            place = data['place']
            browser_id = data['b_id']
            browser_name = data['b_name']
            browser_os = data['b_os']
            image = data['image']
            business_id = data['business_id']

            if(type(image) is InMemoryUploadedFile):
                account  = Account.objects.get(user = user)
                business = Business.objects.get(pk = business_id)

                try:
                    with open(str(os.path.join(BASE_DIR).replace("\\", '/')) + str(account.avatar.url), "rb") as f:
                        enrollments = encode_photo(BytesIO(f.read()))

                    photo  = encode_photo(image.file)
                    match1 = match(photo, enrollments)
                except:
                    return Response({'mark': {'place': None, 'check_in_time': None, 'departure_time': None}, 'error': True}, status=400)

                if(match1[0]):
                    exist_browser = Browser.objects.filter(id = browser_id).exists()
                    if(exist_browser):
                        browser = Browser.objects.get(id = browser_id)
                    else:
                        browser = Browser(id = browser_id, name = browser_name, os = browser_os)
                        browser.save()

                    today = datetime.now().date()
                    exist_mark = account.marks.filter(check_in_time__date = today).exists()
                    
                    if(exist_mark):
                        mark = account.marks.filter(check_in_time__date = timezone.now().date()).first()

                        if(mark.departure_time == None):
                            mark.departure_time = datetime.now()
                            mark.save()
                        
                        serializer = MarkSerializer1(mark)
                        return Response({'mark': serializer.data, 'error': False}, status=200)
                    else:
                        mark = Mark(employee=user, place = place, browser = browser)
                        mark.save()
                        
                        account.marks.add(mark)
                        business.marks.add(mark)
                        serializer = MarkSerializer1(mark)

                        return Response({'mark': serializer.data, 'error': False},status=200)
                else:
                    return Response({'mark': {'place': None, 'check_in_time': None, 'departure_time': None}, 'error': True}, status=400)
            
            return Response(status=200)
        except:
            return Response({'mark': {'place': None, 'check_in_time': None, 'departure_time': None}, 'error': True}, status=400)

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