from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('activities/', views.activities_view, name='activities'),
    
]