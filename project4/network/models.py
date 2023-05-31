from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class User(AbstractUser):
    pass

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    datetime = models.DateTimeField(default=datetime.now())


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    liked_at = models.DateTimeField(default=datetime.now())
  
class Follower(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_follows')
    follows = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_followed_by")
    follow_time = models.DateTimeField(default=datetime.now())
