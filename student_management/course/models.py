from django.db import models
from django.contrib.auth.models import User
from student.models import Student

class Course(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active')
    )
    name = models.CharField(max_length=100, null=True)
    teacher = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    created_by = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course} - {self.student}'