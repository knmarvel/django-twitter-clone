from django.urls import path

from . import views

urlpatterns = [
    path("tweet/", views.tweet, name="tweet"),
    path("all_tweets/", views.all_tweets, name="all_tweets"),
    path("tweet/<int:pk>", views.tweet, name="tweet"),
]
