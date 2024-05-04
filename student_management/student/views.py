from django.shortcuts import render, redirect
from .models import Student
from course.models import Course
from .forms import AddDataForm, UpdateDataForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def dashboard_view(request):
    total_students = Student.objects.all().count()
    total_courses = Course.objects.all().count()

    students_grade1 = Student.objects.filter(grade=1).count()
    students_grade2 = Student.objects.filter(grade=2).count()
    students_grade3 = Student.objects.filter(grade=3).count()

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'students_grade1': students_grade1,
        'students_grade2': students_grade2,
        'students_grade3': students_grade3,
    }

    return render(request, 'student/dashboard.html', context)

@login_required
def student_details_view(request, id):
    try:
        student = Student.objects.get(id=id)
        courses = student.courses.all()
        return render(request, 'student/student_details.html', {'student': student, 'courses': courses})
    except Student.DoesNotExist:
        raise Http404("Student does not exist.")

@login_required
def add_student_view(request):
    if request.method == 'POST':
        form = AddDataForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
        return redirect('student_details', id=student.id)  
    else:
        form = AddDataForm()
    return render(request, 'student/add.html', {'form': form})

@login_required
def list_student_view(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})


@login_required
def search_student_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        students = Student.objects.filter(name__icontains=search_query)
        count = students.count()
        
        context = {
            'students': students, 
            'search_query': search_query,
            'count': count
        }
        return render(request, 'student/search.html', context)

    return render(request, 'student/search.html')

@login_required
def delete_student_view(request):
    students = Student.objects.all()
    return render(request, 'student/delete.html', {'students': students})


@login_required
def delete_student_view2(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist.")
    if request.method == 'POST':
        student.delete()
        return redirect('delete_student')

    return render(request, 'student/delete2.html', {'student': student})

@login_required
def update_student_view(request):
    students = Student.objects.all()
    return render(request, 'student/update.html', {'students': students})

@login_required
def update_student_view2(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateDataForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        return redirect('update_student')
    else:
        form = UpdateDataForm(instance=student)

    return render(request, 'student/update2.html', {'form': form, 'student': student})


