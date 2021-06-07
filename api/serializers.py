from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.ReadOnlyField(source="post.id")

    class Meta:
        fields = ("id", "author", "post", "text", "created")
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset = User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        if attrs["user"] == attrs["following"]:
            raise ValidationError("Self following denied")
        return attrs

    class Meta:
        fields = "__all__"
        model = Follow
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=["user", "following"],
            message="Follow exist"
        )]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group
