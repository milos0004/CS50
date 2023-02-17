from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    #watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    

class Bid(models.Model):
    currentBid = models.IntegerField()
    bidIncrement = models.IntegerField()
    bidListing = models.ForeignKey(Listing, on_delete=models.CASCADE, default="1")
    currentBidUser = models.ForeignKey(User, on_delete=models.CASCADE, default="1")


class Comment(models.Model):
    commentText = models.CharField(max_length=512, null=True)
    commentTime = models.DateTimeField(default=datetime.now, blank=True, editable=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default="1")

