import os

from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join
from django.conf import settings


def get_article_or_404(name: str) -> Template:
    '''
    Return article content as a Django template or raise 404 error
    '''
    try:
        file_path = safe_join(settings.ARTICLE_DIRECTORY, name)
    except ValueError:
        raise Http404('Page not found')
    else:
        if os.path.exists(file_path):
            raise Http404('Page not found')

    with open(file_path) as fp:
        template = Template(fp.read())

    return template


def article(request: HttpRequest, article_name) -> HttpResponse:
    '''
    return the requested article if found
    '''
    filename = '.html'.format(article_name)
    article = get_article_or_404(filename)
    context = {
        'title': article_name,
        'content': article
    }
    return render(request, 'article', context)
