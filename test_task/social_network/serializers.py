from django.contrib.auth.models import User
from rest_framework import serializers
from test_task.social_network.models import Post, Like

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_text', 'publication_date', 'creator']

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'liker', 'like_date']