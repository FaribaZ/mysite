from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lmku#m8&b4+6cuo-%4s_9r&ya=-b@g^ap0g)c9^faxntd+er#_"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# INSTALLED_APPS = INSTALLED_APPS + [
#     'debug-toolbar'
# ]

try:
    from .local import *
except ImportError:
    pass
