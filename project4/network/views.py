from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from datetime import datetime

def calculatelikes(posts):
    likes = []
    for p in posts:
        thelikes = Like.objects.filter(post=p).count()
        print(thelikes)
        likes.append(thelikes)
    return likes

def index(request):
    if request.method == "POST":
        newpost = Post.objects.create(creator=request.user,content=request.POST["post"], datetime= datetime.now())
        newpost.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        posts = Post.objects.all()
        likes = calculatelikes(posts)
        return render(request, "network/index.html", {"posts":posts, "likes":likes})



def follow(request, user):
    u = User.objects.get(username=user)

    f = Follower.objects.create(user=request.user, follows=u,follow_time=datetime.now)
    f.save()



def profile(request, user):
    
    u = User.objects.get(username=user)
    posts = Post.objects.filter(creator=u)
    #filter out all posts created by user logged in
    try:  
        followers = Follower.objects.filter(follows=u)
        #
    except:
        followers = []
    try:
        following = Follower.objects.filter(user=u)
    except:
        following = []

    likes = calculatelikes(posts)
    return render(request, "network/profile.html",{"followers":followers,"following":following,"posts":posts,"user":u,"likes":likes})

def following(request):
    posts=[]
    following = Follower.objects.filter(user=request.user)
    for f in following:
        posts+= Post.objects.filter(creator=f.follows)

    likes = calculatelikes(posts)
    return render(request, "network/following.html",{"posts":posts,"following":following,"likes":likes})




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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
