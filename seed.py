import config
import praw
import collection.models as models
import datetime
import pytz

subreddit_name = 'aww'
time_period = 'month'
limit = 25

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
    models.Submission.objects.create(**model_dict)