from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import GroupClassReview, CoachReview, BusinessReview

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class GroupClassReviewForm(ModelForm):
    class Meta:
        model = GroupClassReview
        fields = ['review', 'comment']

class CoachReviewForm(ModelForm):
    class Meta:
        model = CoachReview
        fields = ['review', 'comment']

class BusinessReviewForm(ModelForm):
    class Meta:
        model = BusinessReview
        fields = ['review', 'comment']

class SearchForm(forms.Form):
    search = forms.CharField(label= 'Search', max_length=50)