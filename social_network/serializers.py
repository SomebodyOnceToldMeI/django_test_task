from django.contrib.auth.models import User
from rest_framework import serializers
from social_network.models import Post, Like

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_text', 'publication_date', 'creator']
        extra_kwargs = {'publication_date' : {'read_only' : True}}

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'liker', 'like_date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}
