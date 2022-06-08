"""tweetus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from tweets.forms import tweetforms
from tweets.views import ( create_view_of_the_tweet, home_page, 
home_page_html, tweet__id,
 tweet__ids, tweet_list, 
 create_view_of_the_tweet_using_rest_api, 
tweet_list_using_rest_api,
tweet_id_detailed_view_using_rest_api,
 to_delete_tweets_from_the_data_base_using_rest_api, 
 tweet_actions_requried,
 )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_html),
    path ('create-tweet', create_view_of_the_tweet_using_rest_api),
    path('tweet/',tweet_list_using_rest_api),
    path('tweet/<int:tweet_id>',tweet_id_detailed_view_using_rest_api),
    path('api/tweet/',include('tweets.urls'))




   # path ('tweet/<int:tweet_id>',home_page),
    # path('t/<int:tweet_id>',tweet__id),# normal way of accessing data base.
    # path('ts/<int:tweet_id>',tweet__ids),#this path is for REST api(accessing database)
    # path('tweet/',tweet_list),#this is for viewing tweet_list
    # path('create-tweet', create_view_of_the_tweet),# this is for creating the tweet.
    # path('api/<int:tweet_id>/delete',to_delete_tweets_from_the_data_base_using_rest_api),
    # path('api/tweet/action',tweet_actions_requried),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#    # path ('tweet/<int:tweet_id>',home_page),
#     path('t/<int:tweet_id>',tweet__id),# normal way of accessing data base.
#     path('ts/<int:tweet_id>',tweet_id_detailed_view_using_rest_api),
#     # path('ts/<int:tweet_id>',tweet__ids),#this path is for REST api(accessing database)
#     path('',home_page_html),
#     # path('tweet/',tweet_list),#this is for viewing tweet_list
#     path('tweet/',tweet_list_using_rest_api),
#     # path('create-tweet', create_view_of_the_tweet),# this is for creating the tweet.
#     path ('create-tweet', create_view_of_the_tweet_using_rest_api),
#     path('api/<int:tweet_id>/delete',to_delete_tweets_from_the_data_base_using_rest_api),
#     path('api/tweet/action',tweet_actions_requried),
# ]
