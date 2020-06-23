# Giant Contact

A re-usable package which can be used in any project that requires a generic `Contact` app. 

This will include the basic formatting and functionality such as model creation via the admin and email sending.

## Installation

To install with the package manager, run:

    $ poetry add giant-contact

You should then add `"contact"` to the `INSTALLED_APPS` in your settings file and to the `Makefile`.  

In `base.py` there should also be a `DEFAULT_FROM_EMAIL` and a `DEFAULT_TO_EMAIL`. This is used by the email sending method.


## Configuration

This application exposes the following settings:

- `DEFAULT_FROM_EMAIL` is the `From` address in the email.
- `DEFAULT_TO_EMAIL` is the default recipient. This is usually the client's address.
- `CONTACT_ABSOLUTE_URL` allows the user to set a different URL as used in the `get_absolute_url` method
- `CONTACT_SUCCESS_URL` allows the user to set a different success URL

- `CONTACT_EMAIL_TEMPLATE_HTML` is the path to the email's HTML representation.
- `CONTACT_EMAIL_TEMPLATE_TXT` is the path to the email's text representation.

- `CONTACT_ADMIN_LIST_DISPLAY` is the field list for the admin index. This must be a list
- `CONTACT_ADMIN_FIELDSETS` allows the user to define the admin fieldset. This must be a list of two-tuples
- `CONTACT_ADMIN_READONLY_FIELDS` allows the user to configure readonly fields in the admin. This must be a list

- `CONTACT_FORM_FIELDS` allows the user to customise what fields are displayed on the contact form. This must be a list
- `CONTACT_FORM_FIELD_PLACEHOLDERS` allows the user to customise the field placeholder text. This must be a dict containing the fieldnames
- `CONTACT_FORM_REQUIRED_FIELDS` allows the user to customise what fields are required on the contact form. This must be a list
- `CONTACT_FORM_LABELS` allows the user to customise what the field labels are on the contact form. This must be a dict of field names and their corresponding label
- `CONTACT_FORM_WIDGETS` allows the user to customise what the field widgets are on the contact form. This must be a dict of field names and their corresponding widget

## URLs

Add the following to `core.urls` for general functionality:

    path("contact/", include("contact.urls"), name="contact"),

If you want to customize the urls to include a different path and/or templates, first you must import `contact.views` in `core.urls` and then you could do add the following:

    path("contact-us/", contact.views.EnquiryFormView.as_view({"template_name": "custom_template_name.html}), name=contact-us)
    path("contact-us/success/", contact.views..SuccessView.as_view(), name=contact-success)
 
 ## Context Processor
 If you wish to use the Contact form with the context processor you will need to add `contact.context_processors.enquiry_form` into the `TEMPLATES` context processors list. This will allow you to access the form in templates.
 
 ## Preparing for release
 
 In order to prep the package for a new release on TestPyPi and PyPi there is one key thing that you need to do. You need to update the version number in the `pyproject.toml`.
 This is so that the package can be published without running into version number conflicts. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.
 
 ## Publishing
 
 Publishing a package with poetry is incredibly easy. Once you have checked that the version number has been updated (not the same as a previous version) then you only need to run two commands.
 
    $ `poetry build` 

will package the project up for you into a way that can be published.
 
    $ `poetry publish`

will publish the package to PyPi. You will need to enter the username and password for the account which can be found in the company password manager
