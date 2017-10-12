from django.db import models
import praw
import datetime
import pytz
from trueskill import Rating

try: 
    import config
except:
    from . import config
    
# Create your models here.
class Submission(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    created_utc = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    score = models.IntegerField()
    subreddit = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ts_mu = models.DecimalField(default=25, max_digits=9, decimal_places=5)
    ts_sigma = models.DecimalField(default=8.333, max_digits=9, decimal_places=5)

    @property
    def ts_rating(self):
        return self.ts_mu - 3 * self.ts_sigma

    @classmethod
    def create(cls, subreddit_name, time_period, limit=30):

        reddit = praw.Reddit(client_id=config.client_id, 
                     client_secret=config.client_secret, 
                     user_agent=config.user_agent)
        
        cols = ['title', 'id', 'url', 'score', 'created_utc']

        for submission in reddit.subreddit(subreddit_name).top(time_period, limit=limit):
            submission_dict = vars(submission)
            model_dict = {i: submission_dict[i] for i in cols}
            model_dict['subreddit'] = submission_dict['subreddit'].display_name
            model_dict['author'] = submission_dict['author'].name
            model_dict['created_utc'] = datetime.datetime.fromtimestamp(model_dict['created_utc']).replace(tzinfo=pytz.UTC)
            print(model_dict)
            cls(**model_dict).save()
