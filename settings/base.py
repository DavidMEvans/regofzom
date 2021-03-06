import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: Enter your own SECRET_KEY here
SECRET_KEY = 'vk95!s^fbcr!65iu*+!a_%mi2b5pfh+=yl!!14unpa(dq7bg2$'

ALLOWED_HOSTS = ['regofzom.herokuapp.com']
SITE_ID = 2

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.template',
    'django_forms_bootstrap',
    'django.contrib.sites',
    'accounts',
    'posts',
    'RegofZom'
]

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailAuth',)
LOGIN_URL = '/login/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.debug_toolbar.middleware.DebugToolbarMiddleware ',
]

ROOT_URLCONF = 'RegZom.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'RegofZom.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

#TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'posts/templates'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "../static/js",
                               "tinymce", "tinymce.min.js")