# -*- coding: UTF-8 -*-

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: company/urls.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: urls of trade module

from django import forms
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.Form):
    author = forms.CharField(label = _('Author'), max_length = 20, required = False)
    email = forms.EmailField(label = _('E-mail'), max_length = 100, required = False)
    url = forms.URLField(label = _('URL'), required = False)
    content = forms.CharField(label = _('Content'), widget = forms.Textarea)
