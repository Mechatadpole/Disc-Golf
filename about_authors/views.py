from django.shortcuts import render, redirect
from django.http import HttpResponse


def members(request):
    return render(request, 'about_authors/group.html')

def work(request):
    return render(request, 'about_authors/process.html')

def site(request):
    return render(request, 'about_authors/goals.html')