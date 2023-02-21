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

    imageURL = models.URLField()
    listingCategory = models.CharField(max_length=10, choices=Categories)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    #watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    def __str__(self):
        return f"{self.listingTitle} - {self.listingCategory}"
    


class Bid(models.Model):
    startBid = models.IntegerField(default="1")
    #bidIncrement = models.IntegerField(default="1")
    bidListing = models.OneToOneField(Listing, on_delete=models.CASCADE, default="1")
    currentBid = models.IntegerField()
    currentBidUser = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    def __str__(self):
        return f"{self.bidListing.listingTitle} - £{self.currentBid}"
    
class WatchList(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    listingID = models.ForeignKey(Listing, on_delete=models.CASCADE, default="1")
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, default="1")


class Comment(models.Model):
    commentText = models.CharField(max_length=512, null=True)
    commentTime = models.DateTimeField(default=datetime.now, blank=True, editable=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default="1")

