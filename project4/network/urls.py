
from django.urls import path

from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("/<int:optional_param>", views.index,name="index"),
    path("following", views.following, name="following"),
    path("following/<int:optional_param>", views.following, name="following"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("profile/<str:user>/<int:optional_param>", views.profile, name="profile"),
    path("follow/<str:user>", views.follow, name="follow"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("like/<int:post>",views.like, name="like"),
    path("edit/<int:post>",views.edit, name="edit")
]
