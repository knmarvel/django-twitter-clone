from django.shortcuts import render, redirect
from tweet.models import Tweet
from notification.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        html = 'notifications.html'
        notes = Notification.objects.filter(notified_user=request.user)
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
        new_notes = notes.filter(viewed=False)
        old_notes = notes.filter(viewed=True)
        new_tweets = Tweet.objects.filter(
            tweet__in=[x.tweet for x in new_notes]).order_by(
                "-creation_date")
        old_tweets = Tweet.objects.filter(
            tweet__in=[x.tweet for x in old_notes]).order_by(
                "-creation_date")
        for note in new_notes:
            note.viewed = True
            note.save()
        return render(request, html, {
            'new_tweets': new_tweets,
            'old_tweets': old_tweets,
            'notifications': notifications})
    return redirect('/login/')
