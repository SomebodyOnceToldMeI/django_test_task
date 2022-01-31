from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_text = models.CharField(max_length=1000)
    creation_date = models.DateTimeField('creation date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')

