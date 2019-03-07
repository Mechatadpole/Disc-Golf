from django.urls import path
from . import views

# All urls used to navigate the different paths in Pages, this being only the Home Page.

urlpatterns = [
    path('', views.home, name='pages-home'),
]