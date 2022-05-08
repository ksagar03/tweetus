from django.conf import settings
from rest_framework import serializers
# Serializers and ModelSerializers are similar to Forms and ModelForms. 
# Unlike forms, they are not constrained to dealing with HTML output, and form encoded input.\
from .models import tweet
max_tweet_length= settings.MAX_TWEET_LENGTH
class tweetserializers(serializers.ModelSerializer):
    class Meta:
        model =tweet
        fields=['content', 'id', ]
       

    def validate_tweet_length(self,value):
            if len(value) > max_tweet_length:
                raise serializers.ValidationError("this tweet is way too long")
            return value
