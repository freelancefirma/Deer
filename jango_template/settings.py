import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'  # Замени

DEBUG = True

ALLOWED_HOSTS = ['deer-lipf.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'app',
]

SITE_ID = 1

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'jango_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'jango_template.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CMS_TEMPLATES = [
    ('base.html', 'Base Template'),
    ('app/index.html', 'App index template'),
]
CMS_CONFIRM_VERSION4 = True
CMS_PERMISSION = False


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Добавлено

