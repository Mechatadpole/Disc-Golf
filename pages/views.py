from django.shortcuts import render
from django.shortcuts import HttpResponse

# When the home function is requested, return users to the Home Page

def home(request):
    return render(request, 'pages/home.html')
