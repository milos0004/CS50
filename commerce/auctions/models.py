from django.contrib.auth.models import AbstractUser
from django.db import models

Categories = (
    ('home','Home'), ('technology','Technology'), ('garden','Garden'),('appliances','Appliances'), 
    ('toys','Toys'),('clothing','Clothing'),('sports','Sports'),('health','Health'),('other','Other')
)
class User(AbstractUser):
    pass

class Listing(models.Model):
    listingTitle = models.CharField(max_length=64)
    listingDescription = models.CharField(max_length=512)
    startBid = models.IntegerField()
    imageURL = models.URLField()
    listingCategory = models.CharField(max_length=10, choices=Categories)
    listingCreator = models.ForeignKey(User, on_delete=models.CASCADE)

    pass

class Bid(models.Model):
    currentBid = models.IntegerField()
    bidIncrement = models.IntegerField()
    #hi
    pass

class Comment(models.Model):
    pass
