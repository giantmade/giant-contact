
SECRET_KEY = "giant-contact"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "giant-contact",
    }
}


INSTALLED_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "mixins",
    "contact",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["contact/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en-gb', 'English'),
]

ROOT_URLCONF = "contact.tests.urls"

DEFAULT_TO_EMAIL = "admin@example.com"
DEFAULT_TO_EMAIL = ["admin@example.com"]