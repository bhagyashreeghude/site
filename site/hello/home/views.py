from email import message
from os import name
from django.contrib import messages
#from pyexpat.errors import messages
import re
#from tkinter.font import names
#from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact

# Create your views here.
def index(request):
    messages.success(request,"this is test message")
    return render(request,'index.html')
    
    #return HttpResponse("this is home page")


def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")


def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email =email,phone =phone,desc =desc,date =datetime.today())
        contact.save()
        messages.success(request,'your msg has been saved')

        
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")