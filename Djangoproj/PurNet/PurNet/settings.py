"""
Django settings for PurNet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4lk2dqkggv+$^+j1j4uk#=d^rzhxsoas3z9unpoynkb4uu%b(='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'course_mang',
    'authy',
    'login',
    'inbox',
    'mang_acct',
    'qa_forums',
    'rate_prof',
    'reset',
    #'homepage',
    'group_mang',
    'tutor',
    'qa',
    'bootstrap3',
    'django_markdown',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
LOGIN_URL = '/signin/'
ROOT_URLCONF = 'PurNet.urls'

WSGI_APPLICATION = 'PurNet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'purdue_network.db'),
    }
}
################
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#filepath that will hold user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT  =  '/static/'
STATIC_URL = '/static/'
##############
MARKDOWN_EDITOR_SKIN = 'simple'

STATICFILES_DIRS = ('',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#os.path.join(os.path.dirname(__file__), 'static',),
#)
    os.path.join(os.path.dirname(__file__), 'static' ,),
    os.path.join(BASE_DIR, "static",'/var/www/static/',),
    #os.path.join(os.path.dirname(__file__), 'static1' ,),
    #'c:/Users/pandidannycn/Documents/CS307/Djangoproj/PurNet/user_homepage/static',
)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates' ,),
    #os.path.join(os.path.dirname(__file__), 'templates1' ,),
    #'c:/Users/pandidannycn/Documents/CS307/Djangoproj/PurNet/user_homepage/templates',
)

# login settings

LOGIN_URL = '/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'

