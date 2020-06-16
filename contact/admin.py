from django.conf import settings
from django.contrib import admin

from . import models


@admin.register(models.Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
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
                        "email",
                        "phone_number",
                        "subject",
                        "message",
                    ]
                },
            ),
            ("Metadata", {"fields": ["created_at", "updated_at"]},),
        ),
    )

    readonly_fields = getattr(
        settings, "CONTACT_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"]
    )
