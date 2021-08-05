from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Course, CourseDescription

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
                messages.error(request, v)
        return redirect("/")
    errors = CourseDescription.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")
    else:
        CourseDescription.objects.create(
            course = Course.objects.create(
                name = request.POST["name"]
            ),
            description = request.POST["description"]
        )
    return redirect('/')

def remove_course(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id),
        "desc": CourseDescription.objects.get(course_id=course_id)
    }
    return render(request, "remove_page.html", context)

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')