from django import forms
from django.conf import settings

from . import models


class EnquiryForm(forms.ModelForm):
    """
    Form class for the Enquiry model.
    """

    required_fields = getattr(settings, "CONTACT_FORM_REQUIRED_FIELDS", [])
    field_placeholders = getattr(settings, "CONTACT_FORM_FIELD_PLACEHOLDERS", {})

    class Meta:
        model = models.Enquiry
        fields = getattr(
            settings,
            "CONTACT_FORM_FIELDS",
            [
                "name",
                "organisation",
                "country",
                "email",
                "phone_number",
                "subject",
                "message",
                "accepted_terms",
            ],
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

        # Update field placeholder
        for field, placeholder in self.field_placeholders.items():
            field = self.fields.get(field)
            field.widget.attrs["placeholder"] = placeholder

    def process(self):
        """
        Process the form and send the email notification to the client
        """

        obj = self.save()
        obj.send_email()

        return obj
