# Django settings for docMan project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Steve Castle', 'steve@tigerhaunt.com'),
     ('Easy Track Support', 'easytrack@drssmail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'drss_db',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 't2ng0d0wn',                  # Not used with sqlite3.
        'HOST': 'drssone.cehytjohsebs.us-west-2.rds.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'
USE_TZ = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

BASE_URL = "https://finance.drssone.com"
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'https://drssone.s3.amazonaws.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/ubuntu/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
AWS_STORAGE_BUCKET_NAME = 'drssone'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FILE_OVERWRITE = False
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://drssone.s3.amazonaws.com/'
STATIC_URL = S3_URL

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&amp;0hf(yqf79lr30p^&amp;dk6o+wap=+y(lo&amp;6sk#djq148_g=*0yt^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'reversion.middleware.RevisionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'docMan.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'docMan.wsgi.application'

TEMPLATE_DIRS = (
    '/home/ubuntu/docMan/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'haystack',
    'drss',
    'task_manager',
    'drss_reporter',
    'rest_framework',
    'social_auth',
    'crispy_forms',
    'storages',
    'south',
    'pagination',
    'sorl.thumbnail',
    'gmapi',
    'report_builder',
    'reversion'
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.contrib.github.GithubBackend',
)
ANONYMOUS_USER_ID = -1
SOCIAL_AUTH_ENABLED_BACKENDS = ('google-oauth2')
GOOGLE_CONSUMER_KEY          = 'drssmail.com'
GOOGLE_CONSUMER_SECRET       = 'dbTRpV13HuDGag3RUM3jLL2k'
SOCIAL_AUTH_SESSION_EXPIRATION = False
GOOGLE_OAUTH2_CLIENT_ID      = '97671542908-e0n871i9mqj8i2bgdejcf5ekvi1id2iq.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'a5s3RMOmQXUjxeRvOtgoytk_'
LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',)
}

AWS_ACCESS_KEY_ID = 'AKIAJQB4CNQ4AO4YVJCA'
AWS_SECRET_ACCESS_KEY = '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'



HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '/home/ubuntu/whoosh',
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
#email
DEFAULT_FROM_EMAIL = 'notifications@drssone.com'

THUMBNAIL_DEBUG = True
