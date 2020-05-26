from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [
    path("", views.EnquiryFormView.as_view(), name="contact-us"),
    path("success/", views.SuccessView.as_view(), name="success",),
]
