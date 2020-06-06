from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views import View
from tweet.forms import TweetForm
from tweet.models import Tweet
from notification.models import Notification
from datetime import datetime
from tweet.helpers import make_notifications


# Create your views here.
def all_tweets(request):
    html = "all_tweets.html"
    all_tweets = Tweet.objects.all().order_by(
                "-creation_date")
    notifications = []
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
    return render(request, html, {
        'all_tweets': all_tweets,
        'notifications': notifications})


def tweet(request, pk):
    html = "tweet_detail.html"
    tweet = Tweet.objects.get(pk=pk)
    notifications = []
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
    return render(request, html, {
        'tweet': tweet,
        'notifications': notifications})


class Add_Tweet(View):
    html = "tweet_form.html"
    form_class = TweetForm

    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, self.html, {"form": form})
        return redirect("/login/")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            filled_form = self.form_class(request.POST)
            if filled_form.is_valid():
                data = filled_form.cleaned_data
                Tweet.objects.create(
                    tweet=data['tweet'],
                    author=request.user,
                    creation_date=datetime.now()
                )
                make_notifications(Tweet.objects.last())
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')),)
        return redirect("/login/")
