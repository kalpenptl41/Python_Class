from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("<h1>Hello this is Home Page for Project</h1>")

def about(request):
	return HttpResponse("<h1 style = text-color; red>Hello this is About US Page for Project</h1>")