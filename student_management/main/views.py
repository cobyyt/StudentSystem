from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def activities_view(request):
    return render(request, 'main/activities.html')

