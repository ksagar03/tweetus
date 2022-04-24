from django import forms
from .models import tweet
max_tweet_length = 10
class tweetforms(forms.ModelForm):
    class Meta:  # this method is used to define the aboxe class format 
        model=tweet
        fields=['content']


    def checking_tweet_length(self):
            content= self.cleaned_data.get("content")
            if len(content) > max_tweet_length:
                raise forms.ValidationError("this tweet is way too long")
            return content 
    