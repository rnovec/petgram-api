
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from petgram.models import Post
from petgram.serializers import PostSerializer
from .models import User
from .serializers import UserSerializer

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        """
        API endpoint that allows update users and profile picture
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if 'picture' in request.data or 'clearAvatar' in request.data:
            instance.picture.delete(save=False)

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def picture(self, request, *args, **kwargs):
        """
        API endpoint that allows remove profile picture
        """
        partial = kwargs.pop('partial', True)
        instance = self.get_object()

        instance.picture.delete(save=False)

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        """
        API endpoint that allows get user's posts
        """
        user_posts = Post.objects.filter(user=pk).order_by('-created')

        page = self.paginate_queryset(user_posts)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data)
