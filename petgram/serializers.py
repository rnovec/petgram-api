
from rest_framework import serializers
from .models import Post, Comment, Like

# Serializers define the API representation.


class PostLikesField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.id


class PostCommentsField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.id


class PostSerializer(serializers.ModelSerializer):
    likes = PostLikesField(
        many=True,
        read_only=True
    )

    comments = PostCommentsField(
        many=True,
        read_only=True
    )

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
