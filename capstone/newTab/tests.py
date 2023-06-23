from django.test import TestCase
from .models import *
# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        u1 =  User.objects.create(username="milos", password="hi", email="milos@gmail.com")
        u2 =  User.objects.create(username="andy", password="hi", email="andy@gmail.com")
        r1 = Routine.objects.create(name="Study Day",user=u1)
        r2 = Routine.objects.create(name="Day Off",user=u1)
        b1 = ParentBlock.objects.create(title="StudyBlock1",description="Study Now",startTime='12:00:00',
                                         duration=60,colour="#0000FF", routine=r1,timeScale=2)
        sb1= SubBlock.objects.create(title="TypingPractice",description="Typing Practice",startTime='12:00:00',
                                         duration=10, parent = b1)
        

    def test_creation(self):
        u1 = User.objects.get(username="milos")
        u2 = User.objects.get(username="andy")
        r1 = Routine.objects.get(name="Study Day")
        r2 = Routine.objects.get(name="Day Off")
        b1 = ParentBlock.objects.get(title="StudyBlock1")
        self.assertEquals(r1, b1.routine)
        self.assertEquals(b1.title, "StudyBlock1")
        sb1 = SubBlock.objects.get(title="TypingPractice")
        self.assertEquals(u1,sb1.parent.routine.user)
       

