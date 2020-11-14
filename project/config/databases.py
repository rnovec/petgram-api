# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

import os
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=0)
