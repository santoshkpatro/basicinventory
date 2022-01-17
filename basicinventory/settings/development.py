from . base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'djangoSecretKey'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
