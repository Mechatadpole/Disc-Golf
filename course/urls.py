from django.urls import path
from . import views

# Alls urls used for navigating through the different Course pages....

urlpatterns = [
    path('', views.home, name='courseHome'),
    path('add/', views.add, name='addCourse'),
    path('reviews/', views.reviews, name='reviewCourse'),
    path('delete/', views.delete, name='deleteCourse')
]