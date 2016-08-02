from django.http import HttpResponse
from django.shortcuts import render

def signup(request):
    #Here we will get the signup info from the html page
    return render(request,"index.html", {})
