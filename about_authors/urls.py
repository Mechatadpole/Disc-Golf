from django.urls import path
from . import views

urlpatterns = [
    path('group-members/', views.members, name='groupHome'),
    path('work-process/', views.work, name='processHome'),
    path('site-goals/', views.site, name='goalsHome'),
]