from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import EnquiryForm
from .models import Enquiry


class EnquiryFormView(CreateView):
    """
    Create CBV that displays the enquiry form
    """

    model = Enquiry
    form_class = EnquiryForm
    template_name = "contact/index.html"
    success_url = reverse_lazy(
        getattr(settings, "CONTACT_SUCCESS_URL", "contact:success")
    )

    def form_valid(self, form):
        """
        Call the form process method when POSTed
        """

        self.object = form.process()
        return HttpResponseRedirect(self.get_success_url())


class SuccessView(TemplateView):
    """
    Template CBV that displays the success page
    """

    template_name = "contact/success.html"
