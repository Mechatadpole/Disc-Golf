from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='course'),
    path('add/', views.add, name='addCourse')
]