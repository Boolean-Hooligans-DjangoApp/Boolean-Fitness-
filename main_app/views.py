from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import Group
from .forms import SignUpForm
from .models import Business, GroupClass, Coach
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReviewForm



class BusinessCreate(CreateView):
    model = Business
    fields = ['name', 'email', 'location', 'business_type', 'business_hours', 'rates']

class BusinessUpdate(UpdateView):
    model = Business
    fields = [ 'email', 'location', 'business_type', 'business_hours', 'rates']

class BusinessDelete(DeleteView):
    model = Business
    success_url = '/businesses/'

class GroupClassCreate(CreateView):
    model = GroupClass
    fields = ['name', 'date', 'description']

class GroupClassUpdate(UpdateView):
    model = GroupClass
    fields = ['date', 'description']
    
class GroupClassDelete(DeleteView):
    model = GroupClass
    success_url = '/groupclasses/'

class CoachCreate(CreateView):
    model = Coach
    fields = ['name', 'email', 'location', 'specialty', 'bio', 'availability' ]

class CoachUpdate(UpdateView):
    model = Coach
    fields = ['name', 'email', 'location', 'specialty', 'bio', 'availability' ]
    
class CoachDelete(DeleteView):
    model = Coach
    success_url = '/coaches/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def business_index(request):
    businesses = Business.objects.all()
    return render(request, 'business/index.html', {'businesses': businesses})

def business_detail(request, business_id):
    business = Business.objects.get(id=business_id)
    return render(request, 'business/detail.html', { 'business' : business })

def groupclass_index(request):
    groupclasses = GroupClass.objects.all()
    return render(request, 'groupclass/index.html', {'groupclasses': groupclasses})

def groupclass_detail(request, groupclass_id):
    groupclass = GroupClass.objects.get(id=groupclass_id)
    review_form = ReviewForm()
    return render(request, 'groupclass/detail.html', { 'groupclass' : groupclass, 'review_form': review_form })

def coach_index(request):
    coaches = Coach.objects.all()
    return render(request, 'coach/index.html', {'coaches': coaches})

def coach_detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coach/detail.html', { 'coach' : coach })

def profile(request):
    return render(request, 'profile/profile.html', { 'profile': profile })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_group = Group.objects.get(name="Test Group 1")
            user.groups.add(user_group)
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign-Up - Please try again'

    form = SignUpForm()
    context = {'form' : form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
def add_review(request, groupclass_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.groupclass_id = groupclass_id
        new_review.save()
    return redirect('detail', groupclass_id=groupclass_id)
