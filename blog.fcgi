#! /home/oudsus/bin/python
# -*-coding:UTF-8-*-#

import sys

sys.path += ['/home/oudsus/lib/python2.6/site-packages/django']
sys.path += ['/home/oudsus/Ouds/blog']

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ouds.settings'

from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler

WSGIServer(WSGIHandler()).run()



