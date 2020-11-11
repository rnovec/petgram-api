from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], name='Get User Info')
    def profile(self, request, pk=None):
        """Get user profile info."""
        profile = get_object_or_404(Profile, user=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Profiles to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-created')
    serializer_class = ProfileSerializer


