from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import login
from django.views import View
from twitteruser.forms import AddTwitterUser
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification


def index(request):
    if request.user.is_authenticated:
        html = "index.html"
        tweets = Tweet.objects.filter(
            author__in=request.user.following.all()).order_by(
                "-creation_date")
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
        return render(request, html, {
            "tweets": tweets,
            'notifications': notifications})
    return redirect("/login/")


class All_Users(View):
    html = "all_users.html"

    def get(self, request):
        users = TwitterUser.objects.all()
        notifications = []
        if request.user.is_authenticated:
            notifications = Notification.objects.filter(
                notified_user=request.user).filter(viewed=False)
        return render(request, self.html, {
            'users': users,
            'notifications': notifications})


class AddUser_View(View):
    form_class = AddTwitterUser
    html = 'adduser_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.html, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            new_user = TwitterUser.objects.last()
            new_user.set_password(raw_password=data['password'])
            new_user.following.add(new_user)
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
        return render(request, self.html, {"form": form})


def user_detail(request, slug):
    html = "user_detail.html"
    viewed_user = TwitterUser.objects.get(slug=slug)
    followers = TwitterUser.objects.filter(following=viewed_user)
    following = False
    user_tweets = Tweet.objects.filter(author=viewed_user).order_by(
                "-creation_date")
    notifications = []
    if request.user.is_authenticated:
        if viewed_user in request.user.following.all():
            following = True
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
    return render(request, html, {
        'viewed_user': viewed_user,
        'following': following,
        'followers': followers,
        'user_tweets': user_tweets,
        'notifications': notifications
        })


def follow_user(request, slug):
    if request.user.is_authenticated:
        my_user = TwitterUser.objects.get(username=request.user.username)
        viewed_user = TwitterUser.objects.get(slug=slug)
        my_user.following.add(viewed_user)
        my_user.save()
    return redirect("/user/" + slug)


def unfollow_user(request, slug):
    if request.user.is_authenticated:
        my_user = TwitterUser.objects.get(username=request.user.username)
        viewed_user = TwitterUser.objects.get(slug=slug)
        my_user.following.remove(viewed_user)
        my_user.save()
    return redirect("/user/" + slug)
