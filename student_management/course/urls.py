from django.urls import path, include
from . import views


urlpatterns = [
    path('addcourse/', views.add_course_view, name='add_course'),
    path('listcourse/', views.list_course_view, name='list_course'),
    path('deletecourse/', views.delete_course_view, name='delete_course'),
    path('searchcourse/', views.search_course_view, name='search_course'),
    path('updatecourse/', views.update_course_view, name='update_course'),
    path('course-details/<int:id>/', views.course_details_view, name='course_details'),
    path('deletecourse/<int:id>/', views.delete_course_view2, name='delete_course2'),
    path('updatecourse/<int:id>/', views.update_course_view2, name='update_course2'),
    path('courseregister/', views.register_course, name='course_registration'),
    path('courseregister/success/', views.registration_success, name='registration_success'),
    
]