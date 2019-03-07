from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courseHome'),
    path('add/', views.add, name='addCourse')
]