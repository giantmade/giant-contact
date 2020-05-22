import pytest
from django.core.mail import EmailMessage

from contact import forms, models


@pytest.mark.django_db
class TestSignupForm:
    """
    Test class for the Enquiry form and it's methods
    """

    def test_form_save(self):
        """
        Test the form saves correctly on submission
        """

        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@company.com",
            "subject": "Subject",
            "message": "Message",
        }

        form = forms.EnquiryForm(data=data)
        form.save()
        assert models.Enquiry.objects.all().count() == 1
        assert models.Enquiry.objects.get(email=data["email"]).first_name == "John"
        assert form.is_valid()

    def test_email_send(self, mocker):
        """
        Test the email is sent on correct form submission
        """

        send_mock = mocker.Mock()
        mocker.patch.object(
            EmailMessage, "send", send_mock,
        )
        obj = models.Enquiry(email="john@company.com",)

        form = forms.EnquiryForm(instance=obj)

        form.instance.send_email()
        send_mock.assert_called_once()
