
from django.http import HttpResponse
from django.http import response
from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect, render
from .models import tweet
import random  
from .forms import tweetforms
from django.utils.http import is_safe_url # is safe url is a built in function of 
# django which is used to check whether the next url(redirected) is the safe url or not
#  we can also provide the url IP address which can be trusted or which are important to us 
# can be saved in the setting.py-> allowed Host.
from django.conf import settings
from .serializers import tweetserializers
allowedhost=settings.ALLOWED_HOSTS # importing allowed host from the settings.py
# Create your views here.

def home_page(request,*args,**kwargs):
    return HttpResponse("<p>hi this is sagar</p>")


def home_page_html(request):
    return render(request, "home_page.html",status=200) #here the .html files have been saved in the
    # templets folder so that whenever we render a request that html page will be loaded 
    # we can set the path of the templets folder in settings.py 
    # {'DIRS':[os.path.join(BASE_DIR,"templets")]} 


def create_view_of_the_tweet_using_rest_api(request,*args, **kwargs): 
    serializer= tweetserializers( data=request.POST or None)
    print("serializer=",serializer.is_valid())
    if serializer.is_valid():
        obj=serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)

def create_view_of_the_tweet(request,*args, **kwargs):
    user = request.user 
    # print("ajax", request.is_ajax())
    #  next we are checking whether the login account is valid or not
    if not request.user.is_authenticated:
        user= None
        if request.is_ajax():
            return JsonResponse({}, status= 401) # if the website returns in aajax format then this condition is used 
        return redirect(settings.LOGIN_URL) # if it is normal http respose then we use this condition

    form=tweetforms(request.POST or None) #this command will accept the tweet using request.post and if 
    # we won't write any thing then it just returns and then it will accept none .
    # tweetforms-is a def which has been imported from the forms.html
    next_url= request.POST.get("next") or None # this variable will be saving the next url where the  
    # webpage is redirecting (i.e when ever we click a button)
    # print("valid", form.is_valid())
    if form.is_valid(): # if the tweet is valid then the tweet will be saved in the database.
        obj=form.save(commit=False)
        obj.user=user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url,allowedhost):
            return redirect(next_url) # this conditon will redirect the webpage to the home page
        # redirect-> it is a shortcut feature of django which can redirect to any specified webpage. 
        form=tweetforms() 
    if form.errors:
         if form.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request,'form.html',context={"form":form})




def tweet_list(request,*args, **kwargs):
    list=tweet.objects.all()
    tw_list=[x.serialize() for x in list] # here for loop is used, this for loop loads the data from the
    # variable "list" and stores in object "data".
    data={
        "isUser": False,                       #this function loads the data from the data base
        "response": tw_list
    }
    return JsonResponse(data) # it return the data in jasonresponse format.
def tweet__id(request,tweet_id,*args,**kwargs):             
    try:                                                   # this function is written only for 
                                                    # understanding purpose . (NOT USED ANYWHERE)
        ids=tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<p>hai this is sagar and the tweet id is {tweet_id}<br><h1>{ids.content} </h1></p>")
# "f-identifier is used to insert a data into the paragraphs" here we are inserting tweet_id
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
        status= 404
    #return JsonResponse(f"<p>hai this is sagar and the tweet id is {data}<br><h1>{ids.content} </h1></p>")
    # this above code will not work since it is in the http response format 
    return JsonResponse(data, status=status)







# def create_view_of_the_tweet(request,*args, **kwargs):
#     print("ajax", request.is_ajax())
#     form=tweetforms(request.POST or None) #this command will accept the tweet using request.post and if 
#     # we won't write any thing then it just returns and then it will accept none .
#     # tweetforms-is a def which has been imported from the forms.html
#     next_url= request.POST.get("next") or None # this variable will be saving the next url where the  
#     # webpage is redirecting (i.e when ever we click a button)
#     if form.is_valid(): # if the tweet is valid then the tweet will be saved in the database.
#         obj=form.save(commit=False)
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)
#         if next_url != None and is_safe_url(next_url,allowedhost):
#             return redirect(next_url) # this conditon will redirect the webpage to the home page
#         # redirect-> it is a shortcut feature of django which can redirect to any specified webpage. 
#         form=tweetforms() 
#     if form.errors:
#          if form.is_ajax():
#             return JsonResponse(form.errors, status=400)
#     return render(request,'form.html',context={'form':form})



