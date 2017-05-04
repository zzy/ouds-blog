# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.template import loader, Context

def home(request):
    
    # 玩家默认语言
    language = request.META["HTTP_ACCEPT_LANGUAGE"].lower()
    if 'zh-cn' in language:
        language = 'zh-cn'
    elif 'zh-tw' in language:
        language = 'zh-tw'
    else:
        language = language[:2]
    
    request.session['django_language'] = language

    c = Context(
            {'language': request.session['django_language'],},
           )
    t = loader.get_template('init.ouds')

    return HttpResponse(t.render(c))
