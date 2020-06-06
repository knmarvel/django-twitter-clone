from django.urls import path
from twitteruser.views import AddUser_View

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("users/", views.all_users, name="all_users"),
    path("user/<str:slug>/follow_user/",
         views.follow_user,
         name="follow_user"),
    path("user/<str:slug>/unfollow_user/",
         views.unfollow_user,
         name="unfollow_user"),
    path("user/<str:slug>/", views.user_detail, name="user_detail"),
    path("adduser/", AddUser_View.as_view(), name="adduser"),
]
