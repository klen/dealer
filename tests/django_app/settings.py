import os.path as op


ROOT_URLCONF = 'tests.django_app.views'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [op.dirname(__file__)],
        'OPTIONS': {'context_processors': [
            'dealer.contrib.django.context_processor',
        ]}
    },
]

MIDDLEWARE = 'dealer.contrib.django.Middleware',

SECRET_KEY = 'i am so secret'
