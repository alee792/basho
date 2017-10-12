from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 
            'created_utc', 
            'title', 
            'url', 
            'score',
            'subreddit', 
            'author' 
            'ts_mu', 
            'ts_sigma'
        )
        model = models.Submission