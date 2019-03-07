from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

def home(request):
    return render(request, 'course/course_list.html')

def add(request):

    if request.method == "POST":
        added_course = models.Item(course_name=request.POST['Course Name'],city=request.POST['City'], holes=request.POST['Holes'], tee_type=request.POST['Tee Type'])
        added_course.save()
        return redirect('courseHome')
    
    return render(request, 'course/course_add.html')
