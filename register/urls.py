from django.urls import path
from . import views

# All urls used for the register app, currently being the base page for signing up users. 
urlpatterns = [
    path('', views.home, name='registerHome'),
]