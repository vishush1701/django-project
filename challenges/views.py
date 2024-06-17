from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
challenges = {
        "jan":"run for 20 mins!!",
        "feb":"do yoga!!"
    }

def index(request):
    months = challenges.keys()
    return  render(request,'challenges/index.html',{"months":months})

def feb(request):
    return HttpResponse("feb")

def redirectedView(reques,month):
    text = "dumb guys!!"
    if month == 1:
        text = "you are number 1 crazy guy"
    return HttpResponse(text)

def redirect(request,month):
    number = 12
    if month == 'vishwa':
        number = 1
    return HttpResponseRedirect(reverse("monthly-challenges",args=[number]))

def monthly_challenge(request,month):
    text = challenges.get(month) or challenges.get("jan")
    return render(request,'challenges/challenge.html',{"text":text,"month":month})