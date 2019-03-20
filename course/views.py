from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

def home(request):
    # when the home function is requested, redirects users to the course_list.html page
    if request.method =="POST":
        added_course = models.Course.objects.get(id=request.POST['id'])
        added_course.play = request.POST['play']
        added_course.save()
        return redirect('courseHome')
    course_list = models.Course.objects.filter(play=False)
    play_course = models.Course.objects.filter(play=True)

    context = {
        'course_list': course_list,
        "play_course": play_course
    }

    return render(request, 'course/course_list.html', context=context)
    

def add(request):
    # when the add function is requested, saves in any inputs of the given prompt on the course/add/ page and then redirects the user to the Couse page.
    if request.method == "POST":
        added_course = models.Course(course_name=request.POST['course_name'],city=request.POST['city'], holes=request.POST['holes'], tee_type=request.POST['tee_type'])
        added_course.save()
        return redirect('courseHome')

    # If nothing is added into the addCourse prompt, reload the course_add.html page for re-entry of the prompt or to exit the page.
    return render(request, 'course/course_add.html')

def delete(request):
    if request.method == "POST":
        added_course = models.Course.objects.get(id=request.POST['id'])
        added_course.delete()
        return redirect('courseHome')


def course_detail(request, course_id):
    ind_course = models.Course.objects.get(id=course_id)
    context = {
        'ind_course': ind_course
    }
    return render(request, 'course/course_detail.html', context=context)

def review(request, review_id):
    if request.method =="POST":
        added_review = models.Review.objects.get(id=request.POST['id'])
        added_review.user = request.POST['user']
        added_review.crse = request.POST['course']
        added_review.thoughts = request.POST['thoughts']
        added_review.save()

        return redirect('reviewCourse')
    review_list = models.Review.objects.get(id=review_id)

    context = {
        "review_list": review_list
    }

    return render(request, 'course/reviews.html', context=context)

def add_review(request):
    if request.method == "POST":
        added_review = models.Review(author=request.POST['user'], thoughts=request.POST['thoughts'], crse=request.POST['course'])
        added_review.save()
        return redirect('reviewCourse')

    return render(request, 'course/reviews.html')