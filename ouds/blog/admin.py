# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.contrib import admin

from ouds.blog.models import Catalog, Tag, Entry, Comment, Blogroll

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_count')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Catalog, CatalogAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Tag, TagAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'edit_date', 'birth_date', 'is_public', 'comments', 'read')
    search_fields = ['title', 'slug', 'body']
    fieldsets = [(None, {'fields': ('title', 'catalog', 'is_public', 'slug', 'input_format', 'body', 'tags', 'comments', 'read')})]
    date_hierarchy = 'edit_date'
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)

admin.site.register(Entry, EntryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'email', 'author', 'time', 'content', 'url', 'ip')

admin.site.register(Comment, CommentAdmin)

class BlogrollAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Blogroll, BlogrollAdmin)
