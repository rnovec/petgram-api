
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from users.models import User

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        pk = request.data['user_id']
        description = request.data['description']
        if 'photo' not in request.data:
            raise ParseError("Empty content")
        user = get_object_or_404(User, id=pk)
        f = request.data['photo']
        post = Post.objects.create(user=user, description=description)
        post.photo.save(f.name, f, save=True)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer