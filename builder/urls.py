from django.conf.urls import url
from .view import page

urlpatterns = (
    url(r'^(?P<name>[\w./-]+)$', page, name='page'),
    url(r'^$', page, name='homepage'),
)
