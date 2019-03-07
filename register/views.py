from django.shortcuts import render
from django.http import HttpResponse

# currently non functional but may be used later
def index(request):
    return render(request, 'register/index.html')

# When home function is requested, redirects users to the register.html page, which is acting as the signup function.
def home(request):
    return render(request, 'register/register.html')

# When the signup function is requested, redirects users to the register.html page, which is where users are able to create their accounts for the site.
def signup(request):
    return render(request, 'register.html')
