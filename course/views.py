from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

def home(request):
    # when the home function is requested, redirects users to the course_list.html page
    if request.method =="POST":
        added_course = models.Course.objects.get(id=request.POST['id'])
        added_course.play = request.POST('play')
        added_course.save()
        return redirect('courseHome')
    course_list_items = models.Course.objects.filter(play=False)
    play_course = models.Course.objects.filter(play=True)

    context = {
        'course_list': course_list_items,
        "play_course": play_course
    }

    return render(request, 'course/course_list.html')
    

def add(request):
    # when the add function is requested, saves in any inputs of the given prompt on the course/add/ page and then redirects the user to the Couse page.
    if request.method == "POST":
        added_course = models.Course(course_name=request.POST['course_name'],city=request.POST['city'], holes=request.POST['holes'], tee_type=request.POST['tee_type'])
        added_course.save()
        return redirect('courseHome')


    
    
    # If nothing is added into the addCourse prompt, reload the course_add.html page for re-entry of the prompt or to exit the page.
    return render(request, 'course/course_add.html')


    

