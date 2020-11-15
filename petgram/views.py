
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from users.models import User
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        """
        Create a Post, save file and set user owner
        """
        # avoid post without image
        if 'photo' not in request.data:
            raise ParseError("Empty content")

        # obtain user instance
        pk = request.data['user_id']
        description = request.data['description']
        user = get_object_or_404(User, id=pk)

        # create user's post and save image
        f = request.data['photo']
        post = Post.objects.create(user=user, description=description)
        post.photo.save(f.name, f, save=True)

        # prepare response
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy an instance and remove file from S3
        """
        instance = self.get_object()
        instance.photo.delete(save=False)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):

        post_comments = Comment.objects.filter(post=pk).order_by('created')

        page = self.paginate_queryset(post_comments)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(post_comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a Comment and set user owner
        """
        # obtain instances
        user_id = request.data['user_id']
        post_id = request.data['post_id']
        message = request.data['message']
        user = get_object_or_404(User, id=user_id)
        post = get_object_or_404(Post, uuid=post_id)

        # create user's comment
        comment = Comment.objects.create(user=user, post=post, message=message)

        # prepare response
        serializer = self.get_serializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Likes to be viewed or edited.
    """
    queryset = Like.objects.all().order_by('-created')
    serializer_class = LikeSerializer
