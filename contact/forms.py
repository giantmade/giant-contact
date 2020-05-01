from django import forms

from . import models


class EnquiryForm(forms.ModelForm):
    """
    Form class for the Enquiry model.
    """

    class Meta:
        model = models.Enquiry
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
        ]

        widgets = {"message": forms.Textarea}

    def process(self):
        """
        Process the form and send the email notification to the client
        """

        obj = self.save()
        obj.send_email()

        return obj
