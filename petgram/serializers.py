
from rest_framework import serializers
from .models import Post, Comment, Like

# Serializers define the API representation.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 1
        exclude = []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        depth = 1
        exclude = []


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = []
