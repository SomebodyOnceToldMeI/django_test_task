from django.shortcuts import render
from rest_framework import viewsets
from social_network.models import Post,Like
from social_network.serializers import PostSerializer, LikeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import permissions
from django.utils import timezone
from rest_framework.response import Response
from social_network.permissions import UserPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            old_like = Like.objects.get(post=post,liker=user)
            return Response({'response': "post is already liked before"})
        except:
            new_like = Like(post = post, liker = user, like_date = timezone.now())
            new_like.save()
            return Response({'response' : "successfully liked"})

    @action(detail=True, methods = ['post'])
    def unlike(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            old_like = Like.objects.get(post=post, liker=user)
            old_like.delete()
            return Response({'response': "post is successfully unliked"})
        except:
            return Response({'response': "post was not liked before"})



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def create(self, request):
        data = request.data
        new_user = User(username=data['username'])
        new_user.set_password(data['password'])
        try:
            new_user.save()
            return Response({'response' : "user is successfully created."})
        except:
            return Response({'response' : "user already exists."})


