"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

# REST FRAMEWORK
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from users.views import UserViewSet
from petgram.views import PostViewSet, CommentViewSet

# REST REGISTRATION
from rest_registration.api.views import (
    register,
    change_password
)

# SIMPLE JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

admin.site.site_header = "Petgram Admin"
admin.site.site_title = "Petgram Admin Portal"
admin.site.index_title = "Welcome to Petgram Administration Portal"
admin.site.site_url = "/api/v1/"

# api router
router = routers.DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

# jwt urls
# http://domain.com/api/v1/token/...

auth_urlpatterns = [
    path('/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/change-password', change_password, name='change_password'),
    path('/register', register, name='register'),
]

# api docs urls
# http://domain.com/api/v1/docs

api_docs = [
    # Swagger
    path('', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    # OpenAPI
    path('/openapi', get_schema_view(
        title="Petgram API docs",
        description="SHM Development Challenge API",
        version="1.0.0",
    ), name='openapi-schema'),

]

# api urls
# http://domain.com/api/v1/

api_urlpatterns = [
    path('/', include(router.urls)),
    path('/accounts', include(auth_urlpatterns)),
    path('/docs', include(api_docs))
]



# http://domain.com/
urlpatterns = [
    path('', admin.site.urls),                 # admin site urls
    path('api/v1', include(api_urlpatterns)),  # api v1.0
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
