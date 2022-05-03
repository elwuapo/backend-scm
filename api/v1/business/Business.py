# Imports Python
# Imports Django
# Imports Django Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Api
from api.models import Business
from api.v1.business.BusinessSLR import BusinessSerializer1


class BusinessAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            business   = Business.objects.get(pk = pk)
            serializer = BusinessSerializer1(business)
            
            return Response(
                { 'business': serializer.data },
                status=200
            )
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