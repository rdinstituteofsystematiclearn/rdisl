from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView, View

from .models import Slider, OurServices, GalleryCategory, Gallery, Client, Testimonial


# Create your views here.


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by("-id")[:5]
        context['our_services'] = OurServices.objects.all()
        context['gallery_category'] = GalleryCategory.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['client'] = Client.objects.all().order_by('-id')
        context['testimonial'] = Testimonial.objects.all().order_by('?')
        return context


class About(TemplateView):
    template_name = 'about-us.html'


class WebDesign(TemplateView):
    template_name = 'website-design.html'


class SoftwareDevelopment(TemplateView):
    template_name = 'software-development.html'


class SEO(TemplateView):
    template_name = 'seo.html'


class ERP(TemplateView):
    template_name = 'erp.html'


class SocialMedia(TemplateView):
    template_name = 'social-media.html'


class MLM(TemplateView):
    template_name = 'mlm-development-india.html'


class BulkSMS(TemplateView):
    template_name = 'Bulk_SMS_Service.html'


class DynamicCRM(TemplateView):
    template_name = 'dynamic-crm-cloud-crm-systems.html'


class ContentManagementSystems(TemplateView):
    template_name = 'ContentManagementSystems.html'


class ContactUs(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, *args, **kwargs):
        pass


class CBE(TemplateView):
    template_name = 'cbe.html'

    def get_context_data(self, **kwargs):
        pass


class RPE(TemplateView):
    template_name = 'rpe.html'

    def get_context_data(self, **kwargs):
        pass


class Recruitement(TemplateView):
    template_name = "recruitment-exam.html"

    def get_context_data(self, **kwargs):
        pass


class ExamPlatefrm(TemplateView):
    template_name = "examination-platefrm.html"

    def get_context_data(self, **kwargs):
        pass


class EntranceExam(TemplateView):
    template_name = "entrance-exam.html"

    def get_context_data(self, **kwargs):
        pass


class Semester(TemplateView):
    template_name = 'semester.html'

    def get_context_data(self, **kwargs):
        pass


class OnlineEvolutionSystem(TemplateView):
    template_name = 'online-evaluation.html'

    def get_context_data(self, **kwargs):
        pass


class OPS(TemplateView):
    template_name = 'online-proctoring-services.html'

    def get_context_data(self, **kwargs):
        pass


class OCS(TemplateView):
    template_name = "online-certification-software.html"

    def get_context_data(self, **kwargs):
        pass


class loginPage(View):
    def get(self, request):
        return render(request, 'rdisl_admin/login.html')

    def post(self, request):
        error = ""
        if request.method == 'POST':
            u = request.POST['uname']
            p = request.POST['pwd']
            user = authenticate(username=u, password=p)
            try:
                if user.is_staff:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        return render(request, 'rdisl_admin/login.html', locals())


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class RegisterNow(TemplateView):
    template_name = 'rdisl_admin/register.html'

    # form_class =CustomerRegistrationFrm
    # success_url = reverse_lazy("loginPage")

    def get_context_data(self, **kwargs):
        pass


class ForgotPassword(TemplateView):
    template_name = 'rdisl_admin/forgot-password.html'

    def get_context_data(self, **kwargs):
        pass


class DashboardView(TemplateView):
    template_name = 'rdisl_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return locals()


class ServicesAdmin(TemplateView):
    template_name = 'rdisl_admin/admin-services.html'

    def get_context_data(self, **kwargs):
        pass


class SliderAdmin(View):
    def get(self, request):
        return render(request, 'rdisl_admin/admin-slider.html')

    def post(self, request):
        error = ""
        if not request.user.is_staff:
            return redirect('loginPage')
        if request.method == "POST":
            si = request.FILES['img']
            title = request.POST['title']
            try:
                Slider.objects.create(slider_img=si, title=title)
                error = 'no'
            except:
                error = 'yes'
        return render(request, 'rdisl_admin/admin-slider.html', locals())


class SliderView(TemplateView):
    template_name = 'rdisl_admin/view-slider.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_staff:
            return redirect('loginPage')
        context['slider'] = Slider.objects.all()
        return context


class Delete_Slider(CreateView):
    def get(self, request, id):
        if not request.user.is_staff:
            return redirect('login')
        doctor = Slider.objects.get(id=id)
        doctor.delete()
        return redirect('SliderView')


class Update_Slider(CreateView):
    def get(self, request, id):
        error = ""
        if not request.user.is_authenticated:
            return redirect('login')
        user = request.user
        slider = Slider.objects.get(id=id)
        if request.method == "POST":
            img = request.POST['img']
            title = request.POST['title']

            slider.slider_img = img
            slider.title = title

            try:
                slider.save()
                error = "no"
            except:
                error = "yes"
        return render(request, 'edit_slider.html', locals())


class ServicesView(TemplateView):
    template_name = 'rdisl_admin/view-services.html'

    def get_context_data(self, **kwargs):
        pass
