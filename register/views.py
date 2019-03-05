from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'register/index.html')

def home(request):
    return HttpResponse('<h1>Register Home</h1>')
