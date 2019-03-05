from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='course-home'),
    path('add/', views.add, name='add-course')
]