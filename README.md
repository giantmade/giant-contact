# Giant Contact

A re-usable package which can be used in any project that requires a generic `Contact` app. 

This will include the basic formatting and functionality such as model creation via the admin and email sending.

## Installation

To install with the package manager, run:

    $ poetry add giant-contact

You should then add `"contact"` to the `INSTALLED_APPS` in `base.py`.  

In `base.py` there should also be a `DEFAULT_FROM_EMAIL` and a `DEFAULT_TO_EMAIL`. This is used by the email sending method.

Add if you're using `django-project-base`, you can add `contact` to the `Makefile` and to run migrations and tests.

## Configuration

This application exposes the following settings:

- `DEFAULT_FROM_EMAIL` is the `From` address in the email.
- `DEFAULT_TO_EMAIL` is the default recipient. This is usually the client's address.

- `CONTACT_EMAIL_TEMPLATE_HTML` is the path to the email's HTML representation.
- `CONTACT_EMAIL_TEMPLATE_TXT` is the path to the email's text representation.

- `CONTACT_ADMIN_LIST_DISPLAY` is the field list for the admin index.
- `CONTACT_ADMIN_FIELDSETS` allows the user to define the admin fieldset.
- `CONTACT_ADMIN_READONLY_FIELDS` allows the user to configure readonly fields in the admin.

## URLs

Add the following to `core.urls` for general functionality:

    path("contact/", include("contact.urls"), namespace=contact)

If you want to customize the urls to include a different path and/or templates, first you must import `contact.views` in `core.urls` and then you could do add the following:

    path("contact-us/", contact.views.EnquiryFormView.as_view({"template_name": "custom_template_name.html}), name=contact-us)
    path("contact-us/success/", contact.views..SuccessView.as_view(), name=contact-success)
 