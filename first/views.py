from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first.models import First
from django.urls import reverse
# Create your views here.

def index(request):
    data = First.objects.all().values()
    return render(request,"index.html",{
        "data":data
    })

def adduser(request):
    return render(request,"adduser.html")

def userdb(request):
    if request.method == "POST":
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        dt = First(First_Name=fname,Last_Name=lname)
        dt.save()
        return HttpResponseRedirect(reverse('home-page'))
    else:
        return HttpResponseRedirect(reverse('add-user'))