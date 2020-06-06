from django.urls import path
from tweet.views import Add_Tweet

from . import views

urlpatterns = [
    path("add_tweet/", Add_Tweet.as_view(), name="add_tweet"),
    path("all_tweets/", views.all_tweets, name="all_tweets"),
    path("tweet/<int:pk>", views.tweet, name="tweet"),
]
