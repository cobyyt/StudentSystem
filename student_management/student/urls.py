from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('addstudent/', views.add_student_view, name='add_student'),
    path('liststudent/', views.list_student_view, name='list_student'),
    path('deletestudent/', views.delete_student_view, name='delete_student'),
    path('searchstudent/', views.search_student_view, name='search_student'),
    path('updatestudent/', views.update_student_view, name='update_student'),
    path('student-details/<int:id>/', views.student_details_view, name='student_details'),
    path('deletestudent/<int:id>/', views.delete_student_view2, name='delete_student2'),
    path('updatestudent/<int:id>/', views.update_student_view2, name='update_student2'),
]