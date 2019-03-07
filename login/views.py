from django.shortcuts import render

# When the home function is requested, redirects users to the login page where they can login to the site.
def home(request):
    return render(request, 'login/login.html')