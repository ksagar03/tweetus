from os import truncate
from django.db import models
import random
# from datetime import date, datetime
# now=datetime.now()
from django.conf import settings
 
users = settings.AUTH_USER_MODEL  

# Create your models here.
class tweet(models.Model):
    user= models.ForeignKey(users, on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
        # here we are specifying blank=True, null=True because when won't add a text and only add a image 
        # error should not be rised.
    image=models.FileField(upload_to='',blank=True, null=True)
    # dates = models.DateTimeField()
    # likes=models.IntegerField(blank=True,null=True)

    class meta:
        ordering= ['-id']
    
    def serialize(x):
        # tw_list=" [{"id":x.id,"contents":x.content,"likes":random.randint(1,100)} " for x in list]
        # insted of above dictionary we can also write-->
        return{
            "id":x.id,
            "contents":x.content,
            "likes":random.randint(1,100),
        }
