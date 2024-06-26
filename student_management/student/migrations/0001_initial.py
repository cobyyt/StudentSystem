# Generated by Django 5.0.4 on 2024-05-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                (
                    "grade",
                    models.PositiveIntegerField(
                        choices=[(1, "1"), (2, "2"), (3, "3")], null=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("birthdate", models.DateField(null=True)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="student_photos"
                    ),
                ),
                (
                    "courses",
                    models.ManyToManyField(
                        through="course.CourseRegistration", to="course.course"
                    ),
                ),
            ],
        ),
    ]
