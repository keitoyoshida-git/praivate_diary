from django.views import generic
from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "diary/index.html" 

class InquiryViews(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm