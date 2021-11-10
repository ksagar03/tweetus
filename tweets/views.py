from django.http import HttpResponse
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from .models import tweet

# Create your views here.

def home_page(request,*args,**kwargs):
    return HttpResponse("<p>hai this is sagar</p>")


def home_page_html(request):
    return render(request, "home_page.html",status=200)

    
def tweet__id(request,tweet_id,*args,**kwargs):
    try:
        ids=tweet.objects.get(id=tweet_id)
    except:
            raise Http404
    return HttpResponse(f"<p>hai this is sagar and the tweet id is {tweet_id}<br><h1>{ids.content} </h1></p>")

 #this is for REST api(accessing database)
    
def tweet__ids(request,tweet_id,*args,**kwargs):
    data={
        'id':tweet_id # this variable is used to store the id which user has given 
        }
    status=200
    try:
        ids=tweet.objects.get(id=tweet_id)
        data['content']=ids.content             # similar to if condition 
    except:
            data['message']="not found please enter the correct id"
            status=404;
    #return JsonResponse(f"<p>hai this is sagar and the tweet id is {data}<br><h1>{ids.content} </h1></p>")
    # this above code will not work since it is in the http response format 
    return JsonResponse(data, status=status)


