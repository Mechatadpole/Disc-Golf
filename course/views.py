from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Course Home</h1>')

def add(request):
    return HttpResponse('<h1>Course Add</h1>')