import pytest
from django.core.mail import EmailMultiAlternatives


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestEnquiry:
    """
    A test class for the enquiry model and it's functionality.
    """

    from contact.models import Enquiry

    def test_str(self):
        """
        Test the str method returns the correct value
        """

        obj = self.Enquiry(first_name="John", last_name="Doe")
        assert str(obj) == "Contact enquiry from John Doe"

    def test_email_send(self, mocker):
        """
        Test the email is sent on correct form submission
        """

        send_mock = mocker.Mock()
        mocker.patch.object(
            EmailMultiAlternatives, "send", send_mock,
        )
        obj = self.Enquiry(email="john@company.com",)

        obj.send_email()
        send_mock.assert_called_once()
