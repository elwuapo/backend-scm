from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from api.v1.sign.Sign import SignIn
from knox import views as KnoxViews

from api.v1.business.Business import BusinessAPI
from api.v1.account.Account import AccountAPI
from api.v1.mark.Mark import MarkAPI
from api.v1.workinghours.WorkingHours import WorkingHoursAPI

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),                                # GET

    # SIGNIN
    path('api/v1/signin/', SignIn.as_view()),                       # POST 

    # SIGNOUT
    path('api/v1/signout/', KnoxViews.LogoutView.as_view()),        # POST                     
    path('api/v1/signout/all/', KnoxViews.LogoutAllView.as_view()), # POST

    # ACCOUNT
    path('api/v1/account/', AccountAPI.as_view()),                  # GET, POST, PUT, DELETE

    # BUSINESS
    path('api/v1/business/<int:pk>/', BusinessAPI.as_view()),       # GET

    # MARK
    path('api/v1/mark/<str:option>/', MarkAPI.as_view()),           # GET
    path('api/v1/mark/', MarkAPI.as_view()),                        # POST

    # WORKING HOURS
    path('api/v1/workinghours/', WorkingHoursAPI.as_view()),                # GET
]   

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)