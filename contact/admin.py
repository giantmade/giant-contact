from django.conf import settings
from django.contrib import admin

from . import models

from mixins.admin import CSVAdminMixin


@admin.register(models.Enquiry)
class EnquiryAdmin(CSVAdminMixin):
    """
    Admin class for displaying the Enquiry model data
    """

    list_display = getattr(
        settings, "CONTACT_ADMIN_LIST_DISPLAY", ["name", "email", "created_at"],
    )

    fieldsets = getattr(
        settings,
        "CONTACT_ADMIN_FIELDSETS",
        (
            (
                "Details",
                {
                    "fields": [
                        "name",
                        "organisation",
                        "country",
                        "email",
                        "phone_number",
                        "subject",
                        "message",
                        "accepted_terms",
                    ]
                },
            ),
            ("Metadata", {"fields": ["created_at", "updated_at"]},),
        ),
    )

    readonly_fields = getattr(
        settings, "CONTACT_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"]
    )
