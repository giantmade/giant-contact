from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from .forms import EnquiryForm
from .models import Contact, Enquiry


class EnquiryFormView(CreateView):
    """
    Create CBV that displays the enquiry form
    """

    model = Enquiry
    form_class = EnquiryForm
    template_name = "contact/contact_us.html"

    def get_success_url(self):
        return self.object.get_absolute_success_url

    def form_valid(self, form):
        """
        Call the form process method when POSTed
        """

        self.object = form.process()

        return HttpResponseRedirect(self.object.get_absolute_success_url)


class SuccessView(TemplateView):
    """
    Template CBV that displays the success page
    """

    template_name = "contact/success.html"
