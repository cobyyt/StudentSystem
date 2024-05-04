from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm

def signup_view(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })
    

def logout_view(request):
    logout(request)
    return redirect('home')