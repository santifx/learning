from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world! <a href=\"about\">About Rango</a> ")
def emery(request):
    return HttpResponse("Rango sees Emery!")
def something(request):
    return HttpResponse("Rango says 'I see something !'")
def about(request):
	return HttpResponse("Rango Says: Here is the about page.\n<a href=\"./\">Return to Main</a> ")
    
