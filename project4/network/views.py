from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from .models import *
from django.core.paginator import Paginator
from datetime import datetime

def calculatelikes(request, posts):
    likes = []
    hasUserLiked = []
    tupleList = []
    for p in posts:
        thelikes = Like.objects.filter(post=p).count()
        li = Like.objects.filter(post=p)
        for l in li:
            if request.user == l.user:
                hasUserLiked.append("https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png")
            else:
                hasUserLiked.append("https://i.ibb.co/k90YGq6/download-removebg-preview.png")

        theTuple = (p,thelikes,hasUserLiked)        
        print(thelikes)
        likes.append(thelikes)
        tupleList.append(theTuple)
    return likes

def createTupleList(request, posts):


    likes = []
    
    tupleList = []

    for p in posts:
        thelikes = Like.objects.filter(post=p).count()
        li = Like.objects.filter(post=p)
        hasUserLiked="https://i.ibb.co/k90YGq6/download-removebg-preview.png"
        for l in li:
            if request.user == l.user:
                hasUserLiked="https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png"
            

        theTuple = (p,thelikes,hasUserLiked)        
        print(thelikes)
        likes.append(thelikes)
        tupleList.append(theTuple)
    return tupleList

    
    likes = []
    
    tupleList = []

    for p in posts:
        thelikes = Like.objects.filter(post=p).count()
        li = Like.objects.filter(post=p)
        hasUserLiked="https://i.ibb.co/k90YGq6/download-removebg-preview.png"
        for l in li:
            if request.user == l.user:
                hasUserLiked="https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png"
            

        theTuple = (p,thelikes,hasUserLiked)        
        print(thelikes)
        likes.append(thelikes)
        tupleList.append(theTuple)
    return tupleList


def index(request):
    if request.method == "POST":
        newpost = Post.objects.create(creator=request.user,content=request.POST["post"], datetime= datetime.now())
        newpost.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        posts = Post.objects.all()
        print(posts)
        paginatedPosts = Paginator(posts,2)
        print(paginatedPosts)
        likes = calculatelikes(request, posts)
        tupleList = createTupleList(request, posts)
        return render(request, "network/index.html", {"posts":posts, "likes":likes,"tuples":tupleList,"paginator":paginatedPosts})

def index(request, optional_param=None):
    if request.method == "POST":
        newpost = Post.objects.create(creator=request.user,content=request.POST["post"], datetime= datetime.now())
        newpost.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        if optional_param:
            pageNo=optional_param
        else:
            pageNo=1
        
        posts = Post.objects.all()
        print(posts)
        paginatedPosts = Paginator(posts,2)
        currentPage=paginatedPosts.page(pageNo)
        currentPagePosts=currentPage.object_list
        print(paginatedPosts )
        print("YOU ARE HERE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(currentPage)
        print(currentPagePosts)
        print(posts)
        likes = calculatelikes(request, posts)
        tupleList = createTupleList(request, currentPagePosts)
        return render(request, "network/index.html", {"posts":posts, "likes":likes,"tuples":tupleList,"paginator":paginatedPosts})



def like(request,post):
    print(post)
    print(int(post))
    thepost= Post.objects.get(id=post)
    if request.method == "POST":
        newlike = Like.objects.create(user=request.user, post=thepost,liked_at=datetime.now())
        newlike.save()
        return HttpResponse(status=204)
    elif request.method == "DELETE":
        like = Like.objects.get(user=request.user,post=thepost)
        like.delete()
        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)



def edit(request,post):
    p = Post.objects.get(id=post)
    if request.method == "PUT":
        data = json.loads(request.body)
        content = data.get("content")
        p.content=content
        p.save()
        return HttpResponse(status=204)

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

    likes = calculatelikes(request,posts)
    text = "Follow User"
    for f in followers:
        if f.user == request.user:
            text="Unfollow"

    tupleList = createTupleList(request, posts)
    return render(request, "network/profile.html",{"followers":followers,"following":following,"posts":posts,"user":u,"likes":likes,"text":text,"tuples":tupleList})

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
