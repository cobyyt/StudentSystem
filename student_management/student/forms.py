from django import forms
from .models import Student
from course.models import Course

class AddDataForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade', 'gender', 'birthdate', 'phone', 'email', 'photo']


class UpdateDataForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade', 'gender', 'birthdate', 'phone', 'email', 'photo']
        
