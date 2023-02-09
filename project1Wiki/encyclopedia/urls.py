from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("wiki/search/", views.search, name="search"),
    #path("wiki/search/<str:entry>", views.entry, name="entry2"),
    path("wiki/new/", views.new, name="new"),
    #path("wiki/new/<str:entry>", views.entry, name="entry3"),
    path("wiki/random/", views.rndm, name="random"),
    path("wiki/<str:entry>/edit/", views.edit, name="edit")
]
