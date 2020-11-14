# Application definition
# https://docs.djangoproject.com/en/3.0/ref/applications/

DJANDO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PART_APPS = [
    'rest_framework',
    'rest_registration',
    'corsheaders',
    'storages',
]

LOCAL_APPS = [
    'users',
    'petgram',
]

INSTALLED_APPS = DJANDO_APPS + THIRD_PART_APPS + LOCAL_APPS
