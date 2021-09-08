from typing import Collection
from django.views import generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    from_class = InquiryForm