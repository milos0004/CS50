from django.test import TestCase
from .models import User, Likes, Post, Followers
# Create your tests here.
class PostTestCase(TestCase):
    u1 =  User.objects.create()