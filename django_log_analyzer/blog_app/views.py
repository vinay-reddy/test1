from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> Blog Home </h1>')

#this is the logic on how we want to handle the request when user goes to the blog home page. we have to match the URL pattern to this view function

def about(request):
    return HttpResponse('<h1> Blog About </h1>')

