# -*- coding: UTF-8 -*-

#============================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#============================================

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail

from ouds.blog.models import Tag, Catalog

tag_dict = {
    'queryset': Tag.objects.all(),
    'template_object_name': 'tag',
}

catalog_dict = {
    'queryset': Catalog.objects.all(),
    'template_object_name': 'catalog',
}

urlpatterns = patterns('ouds.blog.views',
    url(r'^$', 'section', name='blog'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/$', 'entry', name='entry'),
    url(r'^(\d+)/comment/$', 'comment', name='comment'),
    (r'^tag/(?P<slug>[-\w]+)/$', object_detail, dict(tag_dict, template_name='blog/tag_detail.ouds', slug_field='slug')),
    (r'^catalog/(?P<slug>[-\w]+)/$', object_detail, dict(catalog_dict, template_name='blog/catalog_detail.ouds', slug_field='slug')),

    # /archive/ -- archive view for the current year.
    url('^archive/$', 'archive', name='archive'),

    # /archive/2006/ -- archive view for a given year.
    url(r'^archive/(\d{4})/$', 'archive', name='year-archive'),

    # /2006/05/ - entries from a single month.
    # /2006/05/page2 - entries can be paged.
    url(r'^(\d{4})/(\d{2})/(?:page(\d+)/)?$', 'month', name='month'),

    # /2006/05/01 - entries from a single date (also, article permalinks).
    url(r'^(\d{4})/(\d{2})/(\d{2})/$', 'date', name='date'),

    # /page2 - latest entries are paged (back to very first entry).
    url(r'^page(\d+)/$', 'section', name='section'),
    
    # Search Engine
    url(r'^search/$', 'search', name='search'),

     # Tag list
    #(r'^tags/$', 'django.views.generic.list_detail.object_list', dict(tag_dict, paginate_by=15, template_name='blog/tags_list.html')),
    (r'^tags/$', object_list, dict(tag_dict, template_name='blog/tag_list.ouds')),
    #(r'^tags/page-(?P<page>\d+)/$', 'django.views.generic.list_detail.object_list', dict(tag_dict, paginate_by=15, template_name='blog/tags_list.html')),
    url(r'^download/$', direct_to_template, {'template': 'download.ouds'}, name = 'download'),
    url(r'^cert/$', direct_to_template, {'template': 'cert.ouds'}, name = 'cert'),
)

