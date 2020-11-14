from django.db import models
from users.models import User
from uuid import uuid4
from project.storage_backends import PrivateMediaStorage


class Post(models.Model):
    """Post model."""
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(max_length=255)
    photo = models.ImageField(
        storage=PrivateMediaStorage(), blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return description and username."""
        return self.description


class Comment(models.Model):
    """Comment model."""
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    message = models.TextField(blank=True, max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.message, self.user.username)
