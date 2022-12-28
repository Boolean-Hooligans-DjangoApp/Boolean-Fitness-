from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def business_index(request):
    return render(request, 'business/index.html')

def groupclass_index(request):
    return render(request, '')

def profile(request):
    return render(request, 'profile/profile.html', { 'profile': profile })

