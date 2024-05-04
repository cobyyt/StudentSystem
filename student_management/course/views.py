from django.shortcuts import render, redirect
from .models import Course
from .forms import AddDataForm, UpdateDataForm, CourseRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def course_details_view(request, id):
    try:
        course = Course.objects.get(id=id)
        return render(request, 'course/course_details.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404("Course does not exist.")

@login_required
def add_course_view(request):
    if request.method == 'POST':
        form = AddDataForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.created_by = request.user
            course.save()
        return redirect('course_details', id=course.id)  
    else:
        form = AddDataForm()
    return render(request, 'course/add.html', {'form': form})

@login_required
def list_course_view(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

@login_required
def search_course_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        courses = Course.objects.filter(name__icontains=search_query)
        count = courses.count()
        
        context = {
            'courses': courses, 
            'search_query': search_query,
            'count': count
        }
        return render(request, 'course/search.html', context)

    return render(request, 'course/search.html')

@login_required
def delete_course_view(request):
    courses = Course.objects.all()
    return render(request, 'course/delete.html', {'courses': courses})

@login_required
def delete_course_view2(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist.")
    if request.method == 'POST':
        course.delete()
        return redirect('delete_course')

    return render(request, 'course/delete2.html', {'course': course})

@login_required
def update_course_view(request):
    courses = Course.objects.all()
    return render(request, 'course/update.html', {'courses': courses})

@login_required
def update_course_view2(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateDataForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
        return redirect('update_course')
    else:
        form = UpdateDataForm(instance=course)

    return render(request, 'course/update2.html', {'form': form, 'course': course})



@login_required

def register_course(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_reg/registration_course.html', {'form': form})

def registration_success(request):
    return render(request, 'course_reg/registration_success.html')

