from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class User(AbstractUser):
    pass

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    datetime = models.DateTimeField(default=datetime.now())


class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    liked_at = models.DateTimeField(default=datetime.now())
  
class Followers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users_followers')
    followers = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_following")
    follow_time = models.DateTimeField(default=datetime.now())
