from rest_framework import viewsets, status
from social_network.models import Post, Like
from social_network.serializers import PostSerializer, LikeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from social_network.permissions import UserPermission
from django.db.utils import IntegrityError


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response({'status': 'Post does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        try:
            like = Like(post=post, liker=user)
            like.save()
            return Response({'status': "post is successfully liked"})
        except IntegrityError:
            return Response({'status': "post is already liked"})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response({'status': 'Post does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        try:
            old_like = Like.objects.get(post=post, liker=user)
            old_like.delete()
            return Response({'response': "post is successfully unliked"})
        except Like.DoesNotExist:
            return Response({'response': "post was not liked before"})


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


