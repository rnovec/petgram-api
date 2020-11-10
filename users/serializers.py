from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    is_superuser = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'is_superuser', 'groups']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        deep = 1
        exclude = []