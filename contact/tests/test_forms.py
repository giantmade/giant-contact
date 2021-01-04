from contact.tests.conftest import enquiry_instance
import pytest
from django.core.mail import EmailMessage

from contact import forms, models
from . import conftest


@pytest.mark.django_db
class TestSignupForm:
    """
    Test class for the Enquiry form and it's methods
    """

    def test_form_save(self, enquiry_instance):
        """
        Test the form saves correctly on submission
        """

        data = {
            "name": "John Doe",
            "email": "john@company.com",
            "subject": "Subject",
            "message": "Message",
            "country": "United States",
            "accepted_terms": False,
        }

        form = forms.EnquiryForm(data=data)
        form.save()
        assert models.Enquiry.objects.all().count() == 1
        assert models.Enquiry.objects.get(email=data["email"]).name == "John Doe"
        assert form.is_valid()

    def test_email_send(self, mocker, enquiry_instance):
        """
        Test the email is sent on correct form submission
        """

        send_mock = mocker.Mock()
        mocker.patch.object(
            EmailMessage, "send", send_mock,
        )
        form = forms.EnquiryForm(instance=enquiry_instance)

        form.instance.send_email()
        send_mock.assert_called_once()
