import os

from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.utils._os import safe_join


def get_page_or_404(name) -> Template:
    '''
    Return page content as a Django template or raise 404 error.
    '''
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404
    else:
        if not os.path.exists(file_path):
            raise Http404

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def page(request: HttpRequest, name='index') -> HttpResponse:
    '''
    Render the requested page if found.
    '''
    file_name = '{}.html'.format(name)
    page = get_page_or_404(name)
    context = {
        'title': name,
        'page': page
    }
    return render(request, "page.html", context)
