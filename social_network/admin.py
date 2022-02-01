from django.contrib import admin
from social_network.models import Post, Like
# Register your models here.
admin.site.register(Like)
admin.site.register(Post)