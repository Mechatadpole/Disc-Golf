from django.urls import path
from . import views

# All url paths for the login app, being only the Login Page.
urlpatterns = [
    path('', views.home, name='loginHome'),
]