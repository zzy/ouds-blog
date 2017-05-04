# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/settings.py
# Revision: 0.1
# Date: 2007-2-5 17:48
# Description: settings.
#===============================================================================

DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    #(u'长弓骛之', 'ourunix@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oudsus_blog',
        'USER': 'oudsus',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

LOCALE_PATHS = (
    '/home/oudsus/Ouds/blog/locale',
)

LANGUAGES = (
    ('zh-cn', '简体中文'),
    ('zh-tw', '繁體中文'),
    ('en', 'English'),
    ('de', 'Deutsch'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
    ('pt', 'Português'),
    ('es', 'Español'),
    ('sv', 'Svenska'),
    ('ru', 'Русский'),
    ('jp', '日本語'),
    ('ko', '한국어'),
)

MEDIA_ROOT = '/home/oudsus/Ouds/blog/media'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '%zg$h*ibw9t3by1t#bm58jn2&i*^u8@0nu30ow=jw1u-pe93s)'

TEMPLATE_LOADERS = (
                    'django.template.loaders.filesystem.load_template_source',
                    'django.template.loaders.app_directories.load_template_source',
                    )

MIDDLEWARE_CLASSES = (
                      'django.middleware.common.CommonMiddleware',
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      #'django.middleware.cache.CacheMiddleware',
                      'django.middleware.locale.LocaleMiddleware',
                      'django.middleware.doc.XViewMiddleware',
                      )

ROOT_URLCONF = 'ouds.urls'

TEMPLATE_DIRS = (
    '/home/oudsus/Ouds/blog/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    'ouds.utils',
    'ouds.blog',
)

#=====================================
# extend settings
#=====================================

TEMPLATE_STRING_IF_INVALID = "Ouds.biz"
HOST_URL = 'http://Ouds.biz'

SESSION_COOKIE_AGE = 60 * 30 # 30 minutes

#CACHE_BACKEND = 'locmem:///'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_SECONDS = 60 * 5 # 5 minutes
#CACHE_MIDDLEWARE_KEY_PREFIX = 'ouds'

#===============================================================================
# logging
#===============================================================================

#import logging

#FORMAT='[%(asctime)s] %(levelname)s\t%(message)s'
#formatter = logging.Formatter(FORMAT)
#logging.basicConfig(format=FORMAT, level=logging.DEBUG)
