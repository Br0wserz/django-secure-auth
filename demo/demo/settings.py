# Django settings for demo project.

import os

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('root', 'root@local.host'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
    }
}

SECRET_KEY = 'ki02dd*#ff-t(-q6f@b07+7m$xn*noao%r4x0gi(@9m!yxmzl^'
ALLOWED_HOSTS = ['*']
SITE_ID = 1

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Logout, if IP will be changed after auth
    'secureauth.middleware.SecureAuthFixedSessionIPMiddleware',
    # Logout, if session is expired
    'secureauth.middleware.SecureAuthSessionExpireMiddleware',
    # Block IP, if request is not from a real browser
    'secureauth.middleware.SecureAuthTestCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'grappelli',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',

    'bootstrap',
    'djcelery',
    'registration',
    'rosetta',
    'sslserver',

    'secureauth',
    'django_tables2',
    'captcha',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# IMPORTANT: django-secure-auth required configs
AUTH_SMS_FORCE = False
AUTH_SMS_BACKEND = 'Twilio'

# You can register new account on https://www.twilio.com/ and enter
# here demo account settings
AUTH_SMS_BACKEND_AUTH = [
    'ACc73704107c6a5426b2157e279c485d32', 'a2949613dc22aa3df58ea813a6e0747f']

'''
# http://www.smsaero.ru
AUTH_SMS_BACKEND = 'SmsAero'
AUTH_SMS_BACKEND_AUTH = [
    'gotlium@gmail.com', 'c2c6e9d20f59dee59b7a47e39932asfds']
AUTH_SMS_FROM = 'INFORM'

# https://www.twilio.com
AUTH_SMS_BACKEND = 'Twilio'
AUTH_SMS_BACKEND_AUTH = [
    'ACc73704107c6a5426b2157e279c485d32', 'a2949613dc22aa3df58ea813a6e0747f']

# https://www.nexmo.com
AUTH_SMS_BACKEND = 'Nexmo'
AUTH_SMS_BACKEND_AUTH = ['c2e179e1', 'accv1944']
AUTH_SMS_FROM = 'NEXMO'
'''


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/accounts/settings/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
GEOIP_PATH = '/usr/share/GeoIP/'

ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_OPEN = True

CSRF_FAILURE_VIEW = 'demo.csrf_failure'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CAPTCHA_LENGTH = 3
CAPTCHA_FONT_SIZE = 24
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_TIMEOUT = 10
CAPTCHA_LETTER_ROTATION = (-10, 10)
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)

AUTH_TEST_COOKIE_ENABLED = True

# import djcelery
# djcelery.setup_loader()

BROKER_URL = 'redis://127.0.0.1:6379/4'

try:
    from local_settings import *

except ImportError:
    pass
