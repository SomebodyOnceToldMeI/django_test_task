from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=5000)
    publication_date = models.DateTimeField('date published', auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    like_date = models.DateTimeField('date set')

