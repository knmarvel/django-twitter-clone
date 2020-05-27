from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.forms import TweetForm
from tweet.models import Tweet
from datetime import datetime


# Create your views here.
def all_tweets(request):
    html = "all_tweets.html"
    all_tweets = Tweet.objects.all()
    return render(request, html, {'all_tweets': all_tweets})


def tweet(request, pk):
    html = "tweet_detail.html"
    tweet = Tweet.objects.get(pk=pk)
    return render(request, html, {'tweet': tweet})


def add_tweet(request):
    html = "tweet_form.html"
    form = TweetForm()
    if request.method == "POST":
        filled_form = TweetForm(request.POST)
        if form.is_valid():
            data = filled_form.cleaned_data()
            Tweet.objects.create(
                tweet=data['tweet'],
                author=request.user,
                creation_date=datetime.now()
            )
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')),)
    return render(request, html, {"form": form})
