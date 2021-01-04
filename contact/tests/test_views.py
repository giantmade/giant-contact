import pytest
from django.urls import reverse

from contact import models, views

from . import conftest


class TestFormView:
    """
    Test case for the form view
    """

    def test_form(self, client):
        """
        Test the response for the form view
        """

        response = client.get((reverse("contact:contact-us")))
        assert response.status_code == 200
        assert "contact/index.html" in response.template_name

    def test_form_success_url(self, enquiry_instance):
        """
        Test the form redirects correctly on form submission
        """

        enquiry = enquiry_instance
        view = views.EnquiryFormView()
        view.object = enquiry
        success_url = view.get_success_url()

        assert success_url == "/contact/success/"
