
from django.test import TestCase
from .models import *
# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        u1 =  User.objects.create(username="milos", password="hi", email="milos@gmail.com")
        u2 =  User.objects.create(username="andy", password="hi", email="andy@gmail.com")
        p1 = Post.objects.create(creator=u1, content="first post!!! Hi")
        l1 = Like.objects.create(user=u2,post=p1)
        f1 = Follower.objects.create(user= u1, followers= u2)

    def test_post_creation(self):
        u1 = User.objects.get(username="milos")
        u2 = User.objects.get(username="andy")
        u1p = Post.objects.get(creator=u1)
        self.assertEquals(u1p.content, "first post!!! Hi")
        self.assertNotEqual(u1p.creator, u2)
        self.assertNotEqual(u1p.creator,None)

    
    def test_likes(self):
        u1 = User.objects.get(username="milos")
        u2 = User.objects.get(username="andy")
        u1p = Post.objects.get(creator=u1)
        u2l = Like.objects.get(user=u2)
        self.assertEquals(u2l.post, u1p)
        self.assertEquals(u2l.user, u2)
        
    def test_Followers(self):
        u1 = User.objects.get(username="milos")
        u2 = User.objects.get(username="andy")
        u1f = Follower.objects.get(user=u1)
        self.assertEquals(u1f.followers, u2)
        self.assertEquals(u1f.user, u1)