from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy

from mixins.models import PublishingMixin, PublishingQuerySetMixin, TimestampMixin


class Enquiry(TimestampMixin):
    """
    A contact enquiry model for storing the details
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created_at", "last_name"]
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        """
        String representation of the enquiry object
        """

        return f"Contact Enquiry from {self.full_name}"

    def send_email(self):
        """
        Send an email to the admins, notifying of an enquiry
        """

        context = {
            "subject": self.subject,
            "obj": self,
        }

        # Build HTML representation.
        html_result = render_to_string(
            "contact/email/message.html" or settings.CONTACT_EMAIL_TEMPLATE_HTML,
            context={"obj": self},
        )

        # Build text representation.
        txt_result = render_to_string(
            "contact/email/message.txt" or settings.CONTACT_EMAIL_TEMPLATE_TXT,
            context={"obj": self},
        )

        # Build the email.
        message = EmailMultiAlternatives(
            subject=context["subject"],
            body=txt_result,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.DEFAULT_TO_EMAIL,
        )

        message.attach_alternative(content=html_result, mimetype="text/html")
        message.send()

    @property
    def full_name(self):
        """
        Return the full name of the contact
        """

        return f"{self.first_name} {self.last_name}"

    @property
    def get_absolute_url(self):
        """
        Return the absolute URL
        """

        return reverse_lazy("contact:contact-us")

    @property
    def admin_url(self):
        schema = "https" if settings.SECURE_SSL_REDIRECT else "http"
        domain = Site.objects.get_current().domain
        path = reverse("admin:contact_enquiry_change", kwargs={"object_id": self.pk})
        return f"{schema}://{domain}{path}"
