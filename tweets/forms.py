from django import forms
from .models import tweet
from django.conf import settings
max_tweet_length= settings.MAX_TWEET_LENGTH
class tweetforms(forms.ModelForm):
    class Meta:  # this method is used to define the aboxe class format 
        model=tweet
        fields=['content']


    def checking_tweet_length(self):
            content= self.cleaned_data.get("content")
            if len(content) > max_tweet_length:
                raise forms.ValidationError("this tweet is way too long")
            return content 
    