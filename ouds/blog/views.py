# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

"""
Methods for read-only views on the data.

Responsible for displaying things summary and detail views.

Same code Copy from: http://www.pointy-stick.com/blog/

"""

import datetime
import logging

from django import http
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.generic.list_detail import object_list
from django.core.urlresolvers import reverse
from django.db.models import Q

from ouds.settings import HOST_URL
from ouds.blog.models import Entry, Tag, Comment
from ouds.blog.forms import CommentForm

ENTRIES_PER_PAGE = 12

def bad_or_missing(request, msg):
    """
    Return an HTTP 404 response for a date request that cannot possibly exist.
    The 'msg' parameter gives the message for the main panel on the page.
    """
    template = loader.get_template('blog/entry_404.ouds')
    context = RequestContext(request, {'message': msg})
    return http.HttpResponseNotFound(template.render(context))


def entry(request, year, month, day, slug):
    """
    Display a specific entry. Non-public entries can be viewed in this way, too
    (helps with creating new entries).
    """
    # FIXME: ValueError can be raised here.
    start = datetime.datetime(int(year), int(month), int(day), 0, 0, 0)
    end = start + datetime.timedelta(days = 1)

    try:
        this_entry = Entry.published.get(slug = slug, birth_date__range = (start, end))
        this_comment = Comment.objects.filter(entry = this_entry.id).order_by('-time')
    except Entry.DoesNotExist:
        return bad_or_missing(request, _('The entry you have requested does not exist.'))

    try:
        next = this_entry.get_next_by_birth_date()
    except Entry.DoesNotExist:
        next = False
    try:
        previous = this_entry.get_previous_by_birth_date()
    except Entry.DoesNotExist:
        previous = False

    this_entry.read = this_entry.read + 1
    this_entry.save()

    return render_to_response(
                              'blog/entry.ouds',
                              {
                               'host_url': HOST_URL,
                               'entry': this_entry,
                               'next': next,
                               'previous': previous,
                               'comments': this_comment,
                               'comment_form': CommentForm(),
                               }
                              )


def date(request, year, month, day):
    """
    Display all entries for a particular date.
    """
    try:
        start = datetime.datetime(int(year), int(month), int(day), 0, 0, 0)
    except ValueError:
        # Date is out of range (e.g. 31/2/06 or 15/14/06)
        return bad_or_missing(request, 'The date you have requested is not '
                'valid.')
    # FIXME: Normalise the dates.
    end = start + datetime.timedelta(days = 1)
    entries = Entry.published.filter(pub_date__range = (start, end)).order_by('-pub_date')
    if entries.count() == 0:
        return bad_or_missing(request, 'There are no entries for the requested '
                'date (%s).' % start.strftime('%d %B %Y'))

    # Create links to the next and previous date.
    # XXX: This looks a little messy, but that is because I am also creating
    # the links and titles here. There's no ideal place to do this; too
    # presentational for the model, too hard-coded for here.
    try:
        next = Entry.published.filter(pub_date__gte = end).order_by('pub_date').values('pub_date')[0]['pub_date']
        y, m, d = next.year, next.month, next.day
        next_link = reverse('date', args=(y, '%02d' % m, '%02d' % d))
        next_title = next.strftime('%d %B %Y')
    except IndexError:
        next_link = False
        next_title = None
    try:
        previous = Entry.published.filter(pub_date__lt = start).order_by('-pub_date').values('pub_date')[0]['pub_date']
        y, m, d = previous.year, previous.month, previous.day
        previous_link = reverse('date', args=(y, '%02d' % m, '%02d' % d))
        previous_title = previous.strftime('%d %B %Y')
    except IndexError:
        previous_link = False
        previous_title = None

    # FIXME: This template isn't appropriate for this instance. It assumes
    # paged data, which we don't have.
    return render_to_response('blog/entry_list.html',
            {'entry_list': entries,
             'has_next': bool(previous_link),
             'next': next_link,
             'next_title': next_title,
             'has_previous': bool(next_link),
             'previous': previous_link,
             'previous_title': previous_title,
            })


def section(request, page = 0):
    """
    Display a paginated list of all entries (latest first).
    """
    qs = Entry.published.all()

    extra = {}

    return page_display(request, qs, 'blog/entry_list.ouds', extra, page)


def page_display(request, qs, template, extra, page):
    """
    A convenience method that wraps the call to views.generic.object_list and
    provide all of the common parameters.
    """
    if page is None:
        page = 0
    else:
        page = int(page)
    return object_list(request, qs, ENTRIES_PER_PAGE, page, True, template, extra_context = extra, template_object_name = 'entry')


def month(request, year, month, page = 0):
    """
    Display paginated entries for a particular month.
    """
    year = int(year)
    month = int(month)
    try:
        date = datetime.date(year, month, 1)
    except ValueError:
        # Bad date format
        return bad_or_missing(request, 'The month you have requested is not '
                'valid')

    entries = Entry.published.filter(pub_date__year = year,
            pub_date__month = month).order_by('-pub_date')
    if entries.count() == 0:
        return bad_or_missing(request, 'There are no entries for the requested '
                'month (%s).' % date.strftime('%B %Y'))

    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    try:
        next = Entry.published.filter(pub_date__gte =
                next_month).order_by('pub_date').values('pub_date')[0]['pub_date']
        # FIXME: Can't work until reverse() is fixed.
        #next_link = reverse('month', args=(next.year, '%02d' % next.month))
        next_link = '/blog/%s/' % next.strftime('%Y/%m')
        next_title = next.strftime('%B %Y')
    except IndexError:
        next_link = False
        next_title = None
    try:
        previous = Entry.published.filter(pub_date__lt =
                datetime.date(year, month, 1)).order_by('-pub_date').values('pub_date')[0]['pub_date']
        #next_link = reverse('month', args=(previous.year, '%02d' % previous.month))
        previous_link = '/blog/%s/' % previous.strftime('%Y/%m')
        previous_title = previous.strftime('%B %Y')
    except IndexError:
        previous_link = False
        previous_title = None

    extra_links = {
        'next_month': next_link,
        'next_title': next_title,
        'previous_month': previous_link,
        'previous_title': previous_title,
        'total': entries.count(),
        'this_url': '/blog/%04d/%02d/' % (year, month),
    }
    return page_display(request, entries, 'blog/entry_list.html',
            extra_links, page)


def archive(request, year=None):
    """
    Display a summary of available entries for a particular year (defaults to
    the current year).
    """
    if year:
        year = int(year)
    else:
        return http.HttpResponseRedirect(reverse('year-archive',
                args=(datetime.date.today().year,)))

    entry_list = Entry.published.order_by('-birth_date').filter(birth_date__year=year)

    try:
        next = Entry.published.filter(birth_date__gte=datetime.date(year + 1, 1, 1)).order_by('birth_date')[0]
        next = next.birth_date.strftime('%Y')
    except IndexError:
        next = False
    try:
        previous = Entry.published.filter(birth_date__lt=datetime.date(year, 1, 1)).order_by('-birth_date')[0]
        previous = previous.birth_date.strftime('%Y')
    except IndexError:
        previous = False

    return render_to_response('blog/archive.ouds',
            {'year': year,
             'entry_list': entry_list,
             'next': next,
             'previous': previous,
             'latest': str(datetime.date.today().year),
            })



def tag(request, slug, page = 0):
    logging.info("Tags: %s" % (slug))

    try:
        qs = Entry.published.all()
    except Tag.DoesNotExist:
        return bad_or_missing(request, 'The tag you have requested ("%s") '
                'does not exist.' % slug)

    extra = {}
    logging.info(qs)
    return page_display(request, qs, 'blog/entry_list.html', extra, page)


def search(request):
    keyWord = request.GET['KeyWord']
    
    entryList = Entry.published.filter(Q(title__contains=keyWord) | Q(body__contains=keyWord))

    return render_to_response('blog/blog_search.html', {
        'keyWord': keyWord,
        'entryList': entryList,
        })

def comment(request, id):
    
    data = request.POST
    comment_form = CommentForm(data)
    
    if comment_form.is_valid():
        remote_ip = request.META['REMOTE_ADDR']
        logging.info(request.META.keys())

        author = request.POST['author']
        email = request.POST['email']
        url = request.POST['url']
        content = request.POST['content']
    
        entry = Entry.published.get(id = id)
        comment = Comment(entry = entry, author = author, email = email, url = url, content = content, ip = remote_ip)
        comment.save()
        
        entry.comments = entry.comments + 1
        entry.save()
        
    entry_url = request.POST['entry_url']        
    return HttpResponseRedirect(entry_url)

