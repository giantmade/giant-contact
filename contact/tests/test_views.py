import pytest
from django.urls import reverse


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestFormView:
    """
    Test case for the form view
    """

    from contact import models, views

    def test_form(self, client):
        """
        Test the response for the form view
        """

        response = client.get((reverse("contact:contact-us")))
        assert response.status_code == 200
        assert "contact/contact_us.html" in response.template_name

    def test_form_success_url(self):
        """
        Test the form redirects correctly on form submission
        """

        enquiry = self.models.Enquiry.objects.create()
        view = self.views.EnquiryFormView()
        view.object = enquiry
        success_url = view.get_success_url()

        assert success_url == "/contact-us/success/"
