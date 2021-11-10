from django.db import models

# Create your models here.
class tweet(models.Model):
    content=models.TextField(blank=True, null=True)
        # here we are specifying blank=True, null=True because when won't add a text and only add a image 
        # error should not be rised.
    image=models.FileField(upload_to='',blank=True, null=True)