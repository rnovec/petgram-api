"""Users models."""

# Django
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from .managers import UserManager
from project.storage_backends import PrivateMediaStorage


class User(AbstractBaseUser, PermissionsMixin):

    # account fields
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=100, blank=True)

    # profile fields
    picture = models.ImageField(
        storage=PrivateMediaStorage(), blank=True, null=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # management fields
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fullname']

    def __str__(self):
        return self.username

    def get_full_name(self):
        '''
        Returns the user's fullname
        '''
        return self.fullname
