from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy

from mixins.models import TimestampMixin


class Enquiry(TimestampMixin):
    """
    A contact enquiry model for storing the details
    """

    name = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    accepted_terms = models.BooleanField(null=True)  # Using null here as some projects won't be using this field

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        """
        String representation of the enquiry object
        """

        return f"Contact Enquiry from {self.name}"

    @property
    def first_name(self):
        """
        Returns the first name from the name field
        """
        return self.name.split(" ")[0]

    @property
    def last_name(self):
        """
        Returns the last name from the name field
        """
        return self.name.split(" ")[-1]

    def send_email(self):
        """
        Send an email to the admins, notifying of an enquiry
        """

        context = {
            "subject": self.subject or "Contact Enquiry",
            "obj": self,
        }

        # Build HTML representation.
        html_result = render_to_string(
            getattr(
                settings, "CONTACT_EMAIL_TEMPLATE_HTML", "contact/email/message.html"
            ),
            context={"obj": self},
        )

        # Build text representation.
        txt_result = render_to_string(
            getattr(
                settings, "CONTACT_EMAIL_TEMPLATE_TXT", "contact/email/message.txt"
            ),
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
    def get_absolute_url(self):
        """
        Return the absolute URL
        """

        return reverse_lazy(
            getattr(settings, "CONTACT_ABSOLUTE_URL", "contact:contact-us")
        )

    @property
    def admin_url(self):
        schema = "https" if settings.SECURE_SSL_REDIRECT else "http"
        domain = Site.objects.get_current().domain
        path = reverse("admin:contact_enquiry_change", kwargs={"object_id": self.pk})
        return f"{schema}://{domain}{path}"
