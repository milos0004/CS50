from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Routine(models.Model):
    name = models.CharField(max_length=64, default="Routine")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Block(models.Model):
    title = models.CharField(max_length=64, default="Block")
    description = models.CharField(max_length=4096, null=True)
    startTime = models.TimeField(default='12:00:00')
    duration = models.IntegerField(default=60)
    
class ParentBlock(Block):
    colour = models.CharField(max_length=7, default="#0000FF") #stores hex code for the colour
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    timeScale = models.IntegerField(default=1)

class SubBlock(Block):
    parent = models.ForeignKey(ParentBlock, on_delete=models.CASCADE)
