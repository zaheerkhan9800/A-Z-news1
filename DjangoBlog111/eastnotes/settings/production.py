from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'django1',
#        'USER': 'root',
#        'PASSWORD': 'root',
#        'PORT': '3306',
#        'HOST': 'localhost',
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



