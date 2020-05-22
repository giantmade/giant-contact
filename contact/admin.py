from django.conf import settings
from django.contrib import admin

from . import models


@admin.register(models.Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    """
    Admin class for displaying the Enquiry model data
    """

    list_display = [
        "first_name",
        "last_name",
        "email",
        "subject",
        "created_at",
    ] or settings.CONTACT_ADMIN_LIST_DISPLAY

    fieldsets = (
        ("Details", {"fields": ["first_name", "last_name", "email", "subject",]},),
        (
            "Metadata",
            {"fields": ["created_at", "updated_at", "is_published", "publish_at"]},
        ),
    ) or settings.CONTACT_ADMIN_FIELDSETS

    readonly_fields = [
        "created_at",
        "updated_at",
    ] or settings.CONTACT_ADMIN_READONLY_FIELDS
