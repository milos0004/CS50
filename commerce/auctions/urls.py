from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new/", views.new, name="new"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("<int:listing>", views.listing, name="listing"),
    path("<int:listing>/closeListing/", views.closeListing, name="closeListing"),
    path("catergories/", views.categories, name="categories"),
    path("catergories/<str:category>", views.category, name="category")
]

