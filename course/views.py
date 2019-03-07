from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

def home(request):
    # when the home function is requested, redirects users to the course_list.html page
    return render(request, 'course/course_list.html')

def add(request):
    # when the add function is requested, saves in any inputs of the given prompt on the course/add/ page and then redirects the user to the Couse page.
    if request.method == "POST":
        added_course = models.Item(course_name=request.POST['Course Name'],city=request.POST['City'], holes=request.POST['Holes'], tee_type=request.POST['Tee Type'])
        added_course.save()
        return redirect('courseHome')
    # If nothing is added into the addCourse prompt, reload the course_add.html page for re-entry of the prompt or to exit the page.
    return render(request, 'course/course_add.html')
