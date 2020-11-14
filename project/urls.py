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

# REST FRAMEWORK
from rest_framework import routers
from users.views import UserViewSet
from petgram.views import PostViewSet, CommentViewSet

# SIMPLE JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# api router
router = routers.DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

# jwt urls
# http://domain.com/api/v1/token/...

jwt_urlpatterns = [
    path('access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# api urls
# http://domain.com/api/v1/...

api_urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
    path('token/', include(jwt_urlpatterns))
]

# http://domain.com/
urlpatterns = [
    # path('', admin.site.urls),                 # admin site urls
    path('api/v1/', include(api_urlpatterns)), # api v1.0
]

