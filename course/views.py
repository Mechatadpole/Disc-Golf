from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

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

# THIS WAS SUPER ANNOYING
def my_delete(request):
    if request.method == "POST":
        del_course = models.Course.objects.get(id=request.POST['id'])
        del_course.delete()
        return redirect('courseHome')


def course_detail(request, course_id):
    ind_course = models.Course.objects.get(id=course_id)
    review_list = models.Review.objects.filter(crse=ind_course)
    context = {
        'ind_course': ind_course,
        "review_list": review_list
    }
    return render(request, 'course/course_detail.html', context=context)

def review(request):
    if request.method == "POST":
        added_review = models.Review.objects.get(id=request.POST['id'])
        added_review.user = request.POST['user']
        added_review.crse = request.POST['course']
        added_review.thoughts = request.POST['thoughts']
        added_review.save()

        return redirect('reviewCourse')
    review_list = models.Review.objects.all()

    context = {
        "review_list": review_list
    }

    return render(request, 'course/reviews.html', context=context)

def add_review(request):
    if request.method == "POST":
        r_course = models.Course.objects.get(id=request.POST["crse"])
        added_review = models.Review(author=request.user, thoughts=request.POST['thoughts'], crse=r_course)
        added_review.save()
        return redirect('courseInfo', r_course.id)

    return render(request, 'course/course_detail.html')


def review_delete(request):
    if request.method == "POST":
        added_review = models.Review.objects.get(id=request.POST['id'])
        added_review.delete()
        return redirect('reviewCourse')

def index(request):
    if request.method == "POST":
        all_reviews = models.Review.objects.get(id=request.POST['id'])
        all_reviews.save()

    reviews_list = models.Review.objects.filter(publish=True)
    paginator= Paginator(reviews_list, 5)
    page = request.GET.get('page')
    contacts=paginator.get_page(page)

    context = {
        'review_list': contacts,
        'contacts': contacts,
    }

    return render(request, 'course/reviews.html', context=context)