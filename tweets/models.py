from os import truncate
from django.db import models
import random
# from datetime import date, datetime
# now=datetime.now()
from django.conf import settings
 
users = settings.AUTH_USER_MODEL  

# Create your models here.

class tweet_like(models.Model):          #here we have created a separate table to store no of likes 
    user= models.ForeignKey(users, on_delete=models.CASCADE)    
    tweets=models.ForeignKey("tweet", on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)

class tweet(models.Model):
    # this below variable is for storing data of retweet(retweet resembles the parent and child relation ) 
    parent=models.ForeignKey('self',null=True, on_delete=models.SET_NULL)
    user= models.ForeignKey(users, on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
        # here we are specifying blank=True, null=True because when won't add a text and only add a image 
        # error should not be rised.
    image=models.FileField(upload_to='',blank=True, null=True)
    likes=models.ManyToManyField(users, related_name='tweet_user', blank=True, through=tweet_like)
        #  here many to many field means one tweet can have n number of likes from other user

    dates = models.DateTimeField(auto_now_add=True)
    # likes=models.IntegerField(blank=True,null=True)As like function is not yet written
  

    class Meta:    # this meta needs to be in 'Meta' format otherwise it wont work
        ordering = ['-id']



    @property  # this property will return a boolean value i.e it will check whether the tweet as
    # has any retweet tweet 
    def is_retweet(self):
        return self.parent != None 
    
    def serialize(self):
        # tw_list=" [{"id":x.id,"contents":x.content,"likes":random.randint(1,100)} " for x in list]
        # insted of above dictionary we can also write-->
        return{
            "id":self.id,
            "contents":self.content,
            "likes":random.randint(1,100),
        }
