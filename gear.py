import sys
import os

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='a string',
    ROOT_URLCONF='builder.urls',
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'builder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
