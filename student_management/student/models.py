from django.db import models


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=100, null=True)
    grade = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birthdate = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    photo = models.ImageField(upload_to='student_photos', blank=True, null=True)
    
    courses = models.ManyToManyField('course.Course', through='course.CourseRegistration')


    def __str__(self):
        return self.name
    


