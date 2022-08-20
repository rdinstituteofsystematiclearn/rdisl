from django.views.generic.base import TemplateView

from .models import Slider, OurServices, GalleryCategory, Gallery, Client, Testimonial


# Create your views here.


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by('?')
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


class loginPage(TemplateView):
    template_name = 'rdisl_admin/login.html'

    def get_context_data(self, **kwargs):
        pass


class RegisterNow(TemplateView):
    template_name = 'rdisl_admin/register.html'

    def get_context_data(self, **kwargs):
        pass


class ForgotPassword(TemplateView):
    template_name = 'rdisl_admin/forgot-password.html'

    def get_context_data(self, **kwargs):
        pass


class DashboardView(TemplateView):
    template_name = 'rdisl_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        pass


class ServicesView(TemplateView):
    template_name = 'rdisl_admin/admin-services.html'

    def get_context_data(self, **kwargs):
        pass