from django.shortcuts import render, redirect
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        html = 'notifications.html'
        notes = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
        new_tweets = Tweet.objects.filter(
            id__in=[x.tweet.id for x in notes]).order_by(
                "-creation_date")
        for note in notes:
            note.viewed = True
            note.save()
        notified_user = TwitterUser.objects.get(id=request.user.id)
        return render(request, html, {
            'new_tweets': new_tweets,
            'notes': notes,
            'user': notified_user})
    return redirect('/login/')
