from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('index/', Home.as_view(), name='Home'),
    path('about-us/', About.as_view(), name='About'),
    path('contact-us/', ContactUs.as_view(), name='ContactUs'),

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
    path('examination-plate-frm/', ExamPlatefrm.as_view(), name='ExamPlate-frm'),
    path('entrance-exam/', EntranceExam.as_view(), name='EntranceExam'),
    path('semester/', Semester.as_view(), name='Semester'),
    path('online-evaluation-system/', OnlineEvolutionSystem.as_view(), name='OnlineEvolutionSystem'),
    path('online-proctoring-services/', OPS.as_view(), name='OPS'),
    path('online-certification-platform/', OCS.as_view(), name='OCS'),
    path('log-in/', loginPage.as_view(), name='loginPage'),
    path('forgot-password/', ForgotPassword.as_view(), name='ForgotPassword'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin-services/', ServicesAdmin.as_view(), name='AddServices'),
    path('admin-slider/', SliderAdmin.as_view(), name='SliderAdd'),
]
