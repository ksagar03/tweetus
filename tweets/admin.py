from django.contrib import admin

# Register your models here.
from .models import tweet

class tweetadmin(admin.ModelAdmin):
    list_dis=['__str__','users']
    searchfields=['content','user__username','user__email']
    class Meta:
        model=tweet
        
admin.site.register(tweet)

