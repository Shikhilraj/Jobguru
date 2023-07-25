from django.urls import path
from .views import *


urlpatterns=[
    path("",index),
    path("registration/",register),
    path("login/",login),
    path('view user',userprofile),
    path('logout/',logout),
    path('edit_applicant/<int:id>/',userprofile_edit),
    path('company_register/',c_register),
    path('c_login/',c_login),
    path('send/', send_mail_regis),
    path('verify/<auth_token>', verify),
    path('company_list/',registercompany_list),
    path('sendmail/',sendmail),
    path('addjob/',addjob),
    path('listjob/<int:id>/',joblist),
    path("applyjob/<int:id2>/<int:id1>/",applyjob),
    path('viewapplicants/<str:id>/',viewapplicant),
    path('appliedjobs/<int:id>/',appliedjobs)

]