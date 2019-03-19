from django.urls import path
from . import views

# Alls urls used for navigating through the different Course pages....

urlpatterns = [
    path('', views.home, name='courseHome'),
    path('<int:course_id>/', views.course_detail, name='courseInfo'),
    path('add/', views.add, name='addCourse'),
    path('delete/', views.delete, name='deleteCourse'),
    path('review/', views.review, name='reviewCourse'),
    path('add_review/', views.add_review, name='addReview')
]