# Django REST Framework
# https://www.django-rest-framework.org/

import os
import datetime

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

# Django Registration
# https://pypi.org/project/django-registration/

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
}

# Simple JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "USER_ID_FIELD": "id",
    'USER_ID_CLAIM': 'id',
}

# Django Cors Headers
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = os.environ.get("DJANGO_ALLOWED_ORIGINS").split(' ')
