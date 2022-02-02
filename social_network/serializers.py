from django.contrib.auth.models import User
from rest_framework import serializers
from social_network.models import Post, Like


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'liker', 'like_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.HyperlinkedModelSerializer):
    creator = UserSerializer(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = ['url', 'id', 'post_text', 'publication_date', 'creator']
