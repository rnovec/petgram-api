
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

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):

        user_posts = Post.objects.filter(user=pk).order_by('-created')

        page = self.paginate_queryset(user_posts)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data)
