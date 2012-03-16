# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

class Catalog(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), db_index=True)
    post_count = models.IntegerField(_('Post Count'), default=0)
    birth_date = models.DateTimeField(_('Birth Date'), auto_now_add=True)
    edit_date = models.DateTimeField(_('Edit Date'), auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/blog/catalog/%s/" % self.slug

    class Meta:
        verbose_name = _('Catalog Manager')
        verbose_name_plural = _('Catalog Manager')
        ordering = ['-edit_date', '-birth_date', 'name', ]

class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'), db_index=True)
    birth_date = models.DateTimeField(_('Birth Date'), auto_now_add=True)
    edit_date = models.DateTimeField(_('Edit Date'), auto_now_add=True)

    def __unicode__(self):
        return self.name 

    def get_absolute_url(self):
        return "/blog/tag/%s/" % (self.slug)

    class Meta:
        verbose_name = _('Tag Manager')
        verbose_name_plural = _('Tag Manager')

def rst_convertor(input):
    from ouds.docutils.core import publish_parts
    return publish_parts(source=input, writer_name='html4css1')['fragment']

def markdown_convertor(input):
    from ouds.utils import markdown
    return markdown.markdown(input)

class PublicManager(models.Manager):
    """
    A manager that only selects public entries, by default.
    """
    def get_query_set(self):
        return super(PublicManager, self).get_query_set().filter(is_public=True)

class Entry(models.Model):
    DEFAULT_INPUT_FORMAT = 'H'
    ENTRY_FORMATS = (
            (DEFAULT_INPUT_FORMAT, '(X)HTML'),
            ('R', 'Restructured Text'),
            ('M', 'Markdown'),
            )
    CONVERTORS = {
            'R': rst_convertor,
            'M': markdown_convertor,
            }
    
    title = models.CharField(_('Title'), max_length=200)
    catalog = models.ForeignKey(Catalog, related_name='entries', verbose_name=_('Catalog'))
    is_public = models.BooleanField(_('Is Public ?'), default=True)
    slug = models.SlugField(_('Slug'), db_index=True)
    input_format = models.CharField(_('Input Format'), max_length=2, choices=ENTRY_FORMATS, default=DEFAULT_INPUT_FORMAT)
    body = models.TextField(_('Body'),)
    tags = models.ManyToManyField(Tag, related_name='entries', verbose_name=_('Tag'))
    comments = models.IntegerField(_('Comments'), default=0)
    read = models.IntegerField(_('Read'), default=0)
    birth_date = models.DateTimeField(_('Birth Date'), auto_now_add=True)
    edit_date = models.DateTimeField(_('Edit Date'), auto_now_add=True)
    body_converted = models.TextField(_('Body Converted'), blank=True)
    
    objects = models.Manager()
    published = PublicManager()
    
    def __unicode__(self):
        return self.title 
    
    class Meta:
        verbose_name = _('Entry Manager')
        verbose_name_plural = _('Entry Manager')
        ordering = ('-edit_date',)
        get_latest_by = 'edit_date'

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.birth_date.strftime("%Y/%m/%d"), self.slug)
    
    def save(self):
        """
        If the input is in a markup format, store it to html as well, prior to
        saving.
        """
        if self.input_format != self.DEFAULT_INPUT_FORMAT:
            convertor = self.CONVERTORS[self.input_format]
            if self.body:
                self.body_converted = convertor(self.body)
            else:
                self.body_converted = ''
        else:
            self.body_converted = ''
        super(Entry, self).save()
    
    def _get_body_html(self):
        if self.input_format == self.DEFAULT_INPUT_FORMAT:
            return mark_safe(self.body)
        return mark_safe(self.body_converted)
    
    body_html = property(_get_body_html)

    def edited(self):
        """
        Returns True if this record has been edited after creation (editing and
        creation time are at least 60 minutes apart). This is useful for
        working out whether to display the "last edited" time on an entry.
        """
        return (self.edit_date - self.birth_date).seconds > 3600

    def same_day_edit(self):
        """
        Returns True if the entry was edited on the same day as it was created.
        """
        return self.edited() and self.edit_date.date() == self.birth_date.date()

class Comment(models.Model):
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'))
    author = models.CharField(_('Author'), max_length=20, blank=True)
    email = models.EmailField(_('E-mail'), max_length=100, blank=True)
    url = models.URLField(_('URL'), blank=True)
    content = models.TextField(_('Content'))
    time = models.DateTimeField(_('Time'), auto_now=True)
    ip = models.IPAddressField(_('IP'), )

    def __unicode__(self):
        return self.author

    class Meta:
        verbose_name = _('Comment Manager')
        verbose_name_plural = _('Comment Manager')

class Blogroll(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    address = models.URLField(_('Address'),)
    birth_date = models.DateTimeField(_('Birth Date'), auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Blogroll')
        verbose_name_plural = _('Blogroll')

