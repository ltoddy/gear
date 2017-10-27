import os

from django.http import Http404, HttpResponse, HttpRequest
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