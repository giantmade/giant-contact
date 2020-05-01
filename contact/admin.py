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
    ]
    search_fields = ["country", "position"]
    fieldsets = (
        ("Details", {"fields": ["first_name", "last_name", "email", "subject",]},),
        (
            "Metadata",
            {"fields": ["created_at", "updated_at", "is_published", "publish_at"]},
        ),
    )

    readonly_fields = ["created_at", "updated_at"]
