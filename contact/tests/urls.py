from django.urls import include, path
from django.contrib import admin

""""
Url patterns for testing
"""

urlpatterns = [
    path("contact/", include("contact.urls", namespace="contact")),
    path("admin/", admin.site.urls),
]
