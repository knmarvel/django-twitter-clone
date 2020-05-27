from django.urls import path

from . import views

urlpatterns = [
    path("add_tweet/", views.add_tweet, name="add_tweet"),
    path("all_tweets/", views.all_tweets, name="all_tweets"),
    path("tweet/<int:pk>", views.tweet, name="tweet"),
]
