from notification.models import Notification
from twitteruser.models import TwitterUser
import re


def make_notifications(tweet):
    """Determines if any users are mentioned in a tweet;
    if they are, creates a notification for the user."""
    if "@" in tweet.tweet:
        users = find_mentioned_users(tweet.tweet)
        for user in users:
            if user in [x.username for x in TwitterUser.objects.all()]:
                Notification.objects.create(
                    tweet=tweet,
                    notified_user=TwitterUser.objects.get(username=user),
                    viewed=False
                )
    pass


def find_mentioned_users(tweet):
    """Determines if any users are mentioned in a tweet"""
    mentioned_users = re.findall(r"@(\w+)\b", tweet)
    return mentioned_users
