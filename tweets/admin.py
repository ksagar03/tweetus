from django.contrib import admin

# Register your models here.
from .models import tweet, tweet_like

class tweetlikeadmin(admin.TabularInline):
    model=tweet_like

class tweetadmin(admin.ModelAdmin):
    inlines = [tweetlikeadmin]
    list_dis=['__str__','users']
    searchfields=['content','user__username','user__email']
    class Meta:
        model=tweet
        
admin.site.register(tweet)

