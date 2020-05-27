from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import login
from twitteruser.forms import AddTwitterUser
from twitteruser.models import TwitterUser
from tweet.models import Tweet


def index(request):
    if request.user.is_authenticated:
        html = "index.html"
        tweets = Tweet.objects.all()
        return render(request, html, {"tweets": tweets})
    return redirect("/login/")


def all_users(request):
    html = "all_users.html"
    users = TwitterUser.objects.all()
    return render(request, html, {'users': users})


def adduser_view(request):
    if request.method == "POST":
        form = AddTwitterUser(request.POST)
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
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
        return render(request, "adduser_form.html", {"form": form})
    form = AddTwitterUser()
    return render(request, "adduser_form.html", {"form": form})


def user_detail(request, slug):
    html = "user_detail.html"
    viewed_user = TwitterUser.objects.get(slug=slug)
    followers = TwitterUser.objects.filter(following=viewed_user)
    following = False
    if viewed_user in request.user.following.all():
        following = True
    user_tweets = Tweet.objects.filter(author=viewed_user)
    return render(request, html, {
        'viewed_user': viewed_user,
        'following': following,
        'followers': followers,
        'user_tweets': user_tweets,
        })


def follow_user(request, slug):
    my_user = TwitterUser.objects.get(username=request.user.username)
    viewed_user = TwitterUser.objects.get(slug=slug)
    my_user.following.add(viewed_user)
    my_user.save()
    return redirect("/user/" + slug)


def unfollow_user(request, slug):
    my_user = TwitterUser.objects.get(username=request.user.username)
    viewed_user = TwitterUser.objects.get(slug=slug)
    my_user.following.remove(viewed_user)
    my_user.save()
    return redirect("/user/" + slug)
