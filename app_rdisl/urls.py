from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('index/', Home.as_view(), name='Home'),
    path('about-us/', About.as_view(), name='About'),
    path('contact-us/', ContactUs.as_view(), name='ContactUs'),
    path('send-mail/', SendMail.as_view(), name='SendMail'),
    path('website-design/', WebDesign.as_view(), name='Website_Design'),
    path('software-development/', SoftwareDevelopment.as_view(), name='SoftwareDevelopment'),
    path('seo/', SEO.as_view(), name="SEO"),
    path('erp/', ERP.as_view(), name='ERP'),
    path('social-media/', SocialMedia.as_view(), name='SocialMedia'),
    path('mlm/', MLM.as_view(), name='MLM'),
    path('bulk-sms-service/', BulkSMS.as_view(), name='BulkSMS'),
    path('dynamic-crm-cloud-crm-systems/', DynamicCRM.as_view(), name='DynamicCRM'),
    path('content-management-systems/', ContentManagementSystems.as_view(), name='ContentManagementSystems'),
    path('computer-base-examination/', CBE.as_view(), name='cbe'),
    path('remote-proctored-exam/', RPE.as_view(), name='rpe'),
    path('recruitment-exam/', Recruitement.as_view(), name='recruitment'),
    path('examination-platefrm/', ExamPlatefrm.as_view(), name='ExamPlatefrm'),
    path('entrance-exam/', EntranceExam.as_view(), name='EntranceExam'),
    path('semester/', Semester.as_view(), name='Semester'),
    path('online-evalution-system/', OnlineEvolutionSystem.as_view(), name='OnlineEvolutionSystem')
]
