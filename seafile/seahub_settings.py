# -*- coding: utf-8 -*-
SECRET_KEY = "secret key"

#When False the files are served via a Nginx location clause
SERVE_STATIC = False

#Hard coded in clients
#The subdomain "www" is the master domain.
#The site root does 301 to www, which does not work here!
FILE_SERVER_ROOT = 'https://www.XXXXX.dyndns.org/sfa/seafhttp'

MEDIA_URL = '/sfa/media/'
COMPRESS_URL = MEDIA_URL
STATIC_URL = MEDIA_URL + 'assets/'
SITE_ROOT = '/sfa/'
LOGIN_URL = '/sfa/accounts/login/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub1-db',
        'USER': 'seafile1',
        'PASSWORD': '<password>',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

