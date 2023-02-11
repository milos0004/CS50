from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    listingTitle = models.CharField(max_length=64)
    listingDescription = models.CharField(max_length=512)
    startBid = models.IntegerField()
    imageURL = models.URLField()
    listingCategory = models.CharField(max_length=64)


    pass

class Bid(models.Model):
    currentBid = models.IntegerField()
    bidIncrement = models.IntegerField()

    pass

class Comment(models.Model):
    pass