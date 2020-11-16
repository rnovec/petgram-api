
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Post, Comment, Like

# Serializers define the API representation.


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return UserSerializer(value).data


class LikesRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.id


class CommentRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.id


class PostSerializer(serializers.ModelSerializer):

    user = UserRelatedField(read_only=True)

    likes = LikesRelatedField(
        many=True,
        read_only=True
    )

    comments = CommentRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Post
        depth = 1
        exclude = []


class CommentSerializer(serializers.ModelSerializer):

    user = UserRelatedField(read_only=True)
    class Meta:
        model = Comment
        depth = 1
        exclude = []


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = []
