from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets

from .models import Comment, Follow, Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
    )

    def get_queryset(self):
        queryset = Post.objects.all()
        group = self.request.query_params.get("group")
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(post=post, author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    #queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = [filters.SearchFilter]
    search_fields = ["user__username", "following__username"]

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
