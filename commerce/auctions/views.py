from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {"listings":listings})

def watchlist(request):
    if request.method == "POST":
        thelistingid = request.POST["thelistingid"]
        listing = Listing.objects.get(pk=thelistingid)
        try:
            member = WatchList.objects.get(listingID=listing,userID=request.user)
            if member:
                member.delete()
                return render(request, "auctions/listing.html", {"listing":listing, "w":False})
        except:
           w = WatchList(listingID=listing,userID=request.user)
           w.save()   
           return render(request, "auctions/listing.html", {"listing":listing, "w":True})
    
    usersWatchlist = WatchList.objects.filter(userID=request.user)
 
    return render(request, "auctions/watchlist.html", {"usersWatchlist":usersWatchlist})

def listing(request,listing):
    try:
        WatchList.objects.get(listingID=listing,userID=request.user)
        w=True
    except:
        w=False
    b = Bid.objects.get(bidListing=listing)
    l = Listing.objects.get(pk=listing)
    if request.method == "POST":
        newBid = request.POST["newBid"]
        if (b.currentBid < int(newBid)):
            b.currentBid = int(newBid)
            b.currentBidUser = request.user
            b.save()
            
    return render(request, "auctions/listing.html", {"listing":l,"bid":b, "w":w})


def new(request):
    if request.method == "POST":
        Title = request.POST["listingTitle"]
        Description = request.POST["listingDescription"]
        image = request.POST["imageURL"]
        Category = request.POST["listingCategory"]
        creat = request.user
        bid = request.POST["startBid"]
        
        l = Listing(listingTitle=Title,listingDescription=Description,imageURL=image,listingCategory=Category,creator=creat)
        l.save()
        b=Bid(startBid=bid,bidListing=l,currentBid=bid,currentBidUser=creat)
        b.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/new.html")
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
