from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    datetime = models.DateTimeField()

    pass

class Likes(models.Model):
    pass

class Followers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    followers = models.ForeignKey(User,on_delete=models.CASCADE)
    pass