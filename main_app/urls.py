from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('businesses/', views.business_index, name= 'index'),
    path('groupclasses/', views.groupclass_index, name= 'class_index'),
    path('wellnesscoaches/',views.coach_index, name='coach_index'),


]
