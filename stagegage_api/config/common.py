import os
from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Common(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',


        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authorization
        'oauth2_provider',
        'social.apps.django_app.default',
        'rest_framework_social_oauth2',

        # Your apps
        'scripts',
        'users',
        'stagegage',

    )

    # https://docs.djangoproject.com/en/1.8/topics/http/middleware/
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social.apps.django_app.context_processors.backends',
                    'social.apps.django_app.context_processors.login_redirect',
                ],
            },
        },
    ]



    SECRET_KEY = 'Not a secret'
    WSGI_APPLICATION = 'wsgi.application'

    # Allow for less strict handling of urls
    APPEND_SLASH = values.BooleanValue(True)

    # Migrations
    MIGRATION_MODULES = {
        'sites': 'contrib.sites.migrations'
    }

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = DEBUG

    MANAGERS = (
        ("Author", 'garrettdwells@gmail.com'),
    )

    # Postgres
    DATABASES = values.DatabaseURLValue('postgres://localhost/stagegage_api')

    # General
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static Files
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media files
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            # "rq_console": {
            #     "format": "%(asctime)s %(message)s",
            #     "datefmt": "%H:%M:%S",
            # },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            # "rq_console": {
            #     "level": "DEBUG",
            #     "class": "rq.utils.ColorizingStreamHandler",
            #     "formatter": "rq_console",
            #     "exclude": ["%(asctime)s"],
            # },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            },
            # "rq.worker": {
            #     "handlers": ["rq_console"],
            #     "level": "DEBUG"
            # },
        }
    }

    # Custom user app
    AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 25,
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            'oauth2_provider.ext.rest_framework.OAuth2Authentication',
            'rest_framework_social_oauth2.authentication.SocialAuthentication',
        ),
        'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    }

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',
        'rest_framework_social_oauth2.backends.DjangoOAuth2',
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
    )


    # # Push notifications
    # DJANGO_PUSH_NOTIFICATIONS = {
    #     'SERVICE': 'push_notifications.services.zeropush.ZeroPushService',
    #     'AUTH_TOKEN': values.Value('local-development')
    # }

    # # Versatile Image Field
    # VERSATILEIMAGEFIELD_SETTINGS = {
    #     # The amount of time, in seconds, that references to created images
    #     # should be stored in the cache. Defaults to `2592000` (30 days)
    #     'cache_length': 2592000,
    #     'cache_name': 'versatileimagefield_cache',
    #     'jpeg_resize_quality': 70,
    #     'sized_directory_name': '__sized__',
    #     'filtered_directory_name': '__filtered__',
    #     'placeholder_directory_name': '__placeholder__',
    #     'create_images_on_demand': False
    # }

    # Facebook configuration
    SOCIAL_AUTH_FACEBOOK_KEY = '1628663287375931'
    SOCIAL_AUTH_FACEBOOK_SECRET = 'a2487e5cb5fe361e98231e963879d75e'

    # Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook.
    # Email is not sent by default, to get it, you must request the email permission:
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


