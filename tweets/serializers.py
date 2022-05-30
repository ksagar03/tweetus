import re
from django.conf import settings
from django.forms import IntegerField, ValidationError
from rest_framework import serializers
# Serializers and ModelSerializers are similar to Forms and ModelForms. 
# Unlike forms, they are not constrained to dealing with HTML output, and form encoded input.\
from .models import tweet
max_tweet_length= settings.MAX_TWEET_LENGTH
max_action_allowed= settings.MAX_ACTION_ALLOWED
class tweet_action_serializer(serializers.Serializer):
    id =serializers.IntegerField()
    action= serializers.CharField()

    def validation_action(self, value):
        value=value.lower().strip() # this line will convert the value into lower case
        # and this strip will convert Like-> tolike 
        if not value in max_action_allowed:
            raise serializers.ValidationError("please enter the valid action")
        return value


class tweetserializers(serializers.ModelSerializer):
    likes= serializers.SerializerMethodField(read_only =True)# this line will allow to rad the likes
    # it will not allow us to change the likes. 
    class Meta:
        model =tweet
        fields=['content', 'id', 'likes' ]
    def get_likes(self,obj):
        return obj.likes.count()

    def validate_tweet_length(self,value):
            if len(value) > max_tweet_length:
                raise serializers.ValidationError("this tweet is way too long")
            return value
