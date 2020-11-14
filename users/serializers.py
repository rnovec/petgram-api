from rest_framework import serializers
from .models import User

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'password',
                   'groups', 'last_login', 'is_active', 'user_permissions']
