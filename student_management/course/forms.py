from django import forms
from .models import Course, CourseRegistration

class AddDataForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'status']


class UpdateDataForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'status']
        
class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ['student', 'course']
    
    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        course = cleaned_data.get('course')

        if student and course:
            if CourseRegistration.objects.filter(student=student, course=course).exists():
                raise forms.ValidationError("The student has already registered for this course.")

            if course.status == 'Pending':
                raise forms.ValidationError("The course is still pending and cannot be registered.")

        return cleaned_data
