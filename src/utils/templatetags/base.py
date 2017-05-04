# -*- coding: UTF-8 -*-

#================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#================================================

from django import template

register = template.Library()

from django.contrib.sites.models import Site

@register.inclusion_tag('_base/sites.ouds')
def sites():
    '''网站友情链接'''
    
    sites = Site.objects.all()
    
    return {'sites': sites,}

from ouds.blog.models import Entry, Catalog, Blogroll, Tag

# last entry
@register.inclusion_tag('_base/last_entry.ouds')
def last_entry():
    return {'last_entry': Entry.published.order_by('-edit_date')[:12]}

# Catalog List
@register.inclusion_tag('_base/catalog_list.ouds')
def catalog_list():
    return {'catalog_list': Catalog.objects.all()}

# Blogroll List
@register.inclusion_tag('_base/blogroll_list.ouds')
def blogroll_list():
    return {'blogroll_list': Blogroll.objects.all()}

# Tags List
@register.inclusion_tag('_base/tag_list.ouds')
def tag_list():
    return {'tag_list': Tag.objects.all()}
