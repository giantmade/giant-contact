import pytest
from django.core.mail import EmailMultiAlternatives

from contact.models import Contact, Enquiry


@pytest.mark.django_db
class TestEnquiry:
    """
    A test class for the enquiry model and it's functionality.
    """

    def test_str(self):
        """
        Test the str method returns the correct value
        """

        obj = Enquiry(first_name="John", last_name="Doe")
        assert str(obj) == "Contact enquiry from John Doe"

    def test_email_send(self, mocker):
        """
        Test the email is sent on correct form submission
        """

        send_mock = mocker.Mock()
        mocker.patch.object(
            EmailMultiAlternatives, "send", send_mock,
        )
        obj = Enquiry(email="john@company.com",)

        obj.send_email()
        send_mock.assert_called_once()
