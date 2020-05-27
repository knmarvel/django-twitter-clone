from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your models here.
class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    notified_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    viewed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "Notification about " + self.tweet.tweet
