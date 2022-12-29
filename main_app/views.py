from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms  import UserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def business_index(request):
    return render(request, 'business/index.html')

def groupclass_index(request):
    return render(request, 'groupclass/index.html')

def coach_index(request):
    return render(request, 'coach/index.html', { 'coach_index': coach_index })

def profile(request):
    return render(request, 'profile/profile.html', { 'profile': profile })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign-Up - Please try again'

    form = UserCreationForm()
    context = {'form' : form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    

