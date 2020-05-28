from django.urls import path

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
    path("adduser/", views.adduser_view, name="adduser"),
]
