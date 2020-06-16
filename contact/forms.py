from django import forms
from django.conf import settings

from . import models


class EnquiryForm(forms.ModelForm):
    """
    Form class for the Enquiry model.
    """
    required_fields = getattr(settings, "CONTACT_FORM_REQUIRED_FIELDS", [])

    class Meta:
        model = models.Enquiry
        fields = getattr(
            settings,
            "CONTACT_FORM_FIELDS",
            ["name", "organisation", "email", "phone_number", "subject", "message",],
        )
        labels = getattr(settings, "CONTACT_FORM_LABELS", None)
        widgets = getattr(settings, "CONTACT_FORM_WIDGETS", None)

    def __init__(self, *args, **kwargs):
        """
        Override the init method to set the customised required fields
        """
        super().__init__(*args, **kwargs)

        # Update the required fields
        for field in self.required_fields:
            self.fields[field].required = True

    def process(self):
        """
        Process the form and send the email notification to the client
        """

        obj = self.save()
        obj.send_email()

        return obj
