from django.shortcuts import render
from django.shortcuts import HttpResponse

# When the home function is requested, return users to the Home Page

def home(request):
    return render(request, 'pages/home.html')

def members(request):
    return render(request, 'pages/group.html')

def work(request):
    return render(request, 'pages/process.html')

def site(request):
    return render(request, 'pages/goals.html')
