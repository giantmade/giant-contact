import pytest
from django.core.mail import EmailMultiAlternatives
from contact.models import Enquiry

from . import conftest


class TestEnquiry:
    """
    A test class for the enquiry model and it's functionality.
    """

    def test_str(self, enquiry_instance):
        """
        Test the str method returns the correct value
        """

        obj = enquiry_instance
        assert str(obj) == "Contact Enquiry from John Doe"

    @pytest.mark.django_db
    def test_email_send(self, mocker, enquiry_instance):
        """
        Test the email is sent on correct form submission
        """

        send_mock = mocker.Mock()
        mocker.patch.object(
            EmailMultiAlternatives, "send", send_mock,
        )

        enquiry_instance.send_email()
        send_mock.assert_called_once()

    def test_first_name(self, enquiry_instance):
        """
        Test the first name method correctly splits and returns the first
        name
        """
        obj = enquiry_instance

        assert obj.first_name == "John"

    def test_last_name(self, enquiry_instance):
        """
        Test the last name method correctly splits and returns the last
        name
        """
        obj = enquiry_instance

        assert obj.last_name == "Doe"
