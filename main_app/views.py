from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .forms import SignUpForm
from .models import Business, GroupClass, Coach, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GroupClassReviewForm, BusinessReviewForm, CoachReviewForm



class BusinessCreate(CreateView):
    model = Business
    fields = ['name', 'email', 'location', 'business_type', 'business_hours', 'rates']


class BusinessUpdate(UpdateView):
    model = Business
    fields = ['email', 'location', 'business_type', 'business_hours', 'rates']


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
    fields = ['name', 'email', 'location', 'specialty', 'bio', 'availability']
    success_url = '/coaches/'


class CoachUpdate(UpdateView):
    model = Coach
    fields = ['name', 'email', 'location', 'specialty', 'bio', 'availability']
    success_url = '/coaches/'


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
    review_form = BusinessReviewForm()
    return render(request, 'business/detail.html', {'business': business
, 'review_form': review_form})


def groupclass_index(request):
    groupclasses = GroupClass.objects.all()
    return render(request, 'groupclass/index.html', {'groupclasses': groupclasses})


def groupclass_detail(request, groupclass_id):
    groupclass = GroupClass.objects.get(id=groupclass_id)
    review_form = GroupClassReviewForm()
    return render(request, 'groupclass/detail.html', {'groupclass': groupclass, 'review_form': review_form})


def coach_index(request):
    coaches = Coach.objects.all()
    return render(request, 'coach/index.html', {'coaches': coaches})


def coach_detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    review_form = CoachReviewForm()
    return render(request, 'coach/detail.html', {'coach': coach, 'review_form': review_form})


def profile(request):
    return render(request, 'profile/profile.html', {'profile': profile})

def upgrade_profile(request):
    print("it worked")
    user_group, _ = Group.objects.get_or_create(name="Business Account")
    bus_add_perm = Permission.objects.get(name='Can add business')
    bus_change_perm = Permission.objects.get(name='Can change business')
    bus_delete_perm = Permission.objects.get(name='Can delete business')
    user_group.permissions.add(bus_add_perm, bus_change_perm, bus_delete_perm)
    request.user.groups.add(user_group)
    return render(request, 'profile/profile.html', {'profile': profile})

def downgrade_profile(request):
    user_group, _ = Group.objects.get_or_create(name="Business Account")
    request.user.groups.remove(user_group)
    return render(request, 'profile/profile.html', {'profile': profile})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_group, _ = Group.objects.get_or_create(name="Default User")
            bus_view_perm = Permission.objects.get(name='Can view business')
            group_view_perm = Permission.objects.get(name='Can view group class')
            coach_view_perm = Permission.objects.get(name='Can view coach')
            review_view_perm = Permission.objects.get(name='Can view review')
            user_group.permissions.add(bus_view_perm, group_view_perm, coach_view_perm, review_view_perm)
            user.groups.add(user_group)
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign-Up - Please try again'

    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def add_groupclass_review(request, groupclass_id):
    form = GroupClassReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.groupclass_id = groupclass_id
        new_review.save()
    return redirect('class_detail', groupclass_id=groupclass_id)

def add_coach_review(request, coach_id):
    form = CoachReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.coach_id = coach_id
        new_review.save()
    return redirect('coach_detail', coach_id=coach_id)

def add_business_review(request, business_id):
    form = BusinessReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.business_id = business_id
        new_review.save()
    return redirect('business_detail', business_id=business_id)