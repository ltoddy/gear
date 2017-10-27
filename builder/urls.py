from django.conf.urls import url
from .views import article

urlpatterns = (
    url(r'^$', article, name='home'),
    url(r'^(?P<article_name>[\w./-]+)$', article, name='article')
)
