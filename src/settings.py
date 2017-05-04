# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/settings.py
# Revision: 0.1
# Date: 2007-2-5 17:48
# Description: settings.
#===============================================================================

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('长弓骛之', 'postmaster@gaiding.com'),
          )

MANAGERS = ADMINS

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'blog',
                'USER': 'ouds',
                'PASSWORD': '',
                'HOST': '',
                'PORT': ''
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

LOCALE_PATHS = (
                '../locale',
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
             ('ko', u'한국어'),
            )

MEDIA_ROOT = '../media'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'h&7f*7_+p6*tau&fulri2ga1(@5vh%6%4(2!lz5c1w!-t%b57t'

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
                 '../templates',
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

#===============================================================================
# extend settings
#===============================================================================

TEMPLATE_STRING_IF_INVALID = "www.ouds.cn"
HOST_URL = 'http://www.ouds.cn'

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

