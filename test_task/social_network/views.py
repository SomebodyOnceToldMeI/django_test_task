from django.shortcuts import render
from rest_framework import viewsets
from test_task.social_network.models import Post,Like
from test_task.social_network.serializers import PostSerializer, LikeSerializer
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('publication_date')
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer