Giant Contact
===================
A small, re-usable package which can be used in any project that requires a generic `Contact` app. 
This will include the basic formatting and functionality such as model creation via the admin and email sending.

Installation
===================

To install with the package manager simply run

    $ poetry add giant-contact

You should then add `"contact"` to the `INSTALLED_APPS` in `base.py`. Copy the templates folder into the correct directory,
this should be something like `src/core/templates/contact` and remove the current templates directory. In `base.py` there should also
be a `DEFAULT_FROM_EMAIL` and a `DEFAULT_TO_EMAIL`. This is used by the email sending method.

Add `contact` to the `makefile` and run migrations once the models are set up how you would like.


