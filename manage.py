import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
    ROOT_URLCONF='builder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
    ARTICLE_DIRECTORY=''
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
