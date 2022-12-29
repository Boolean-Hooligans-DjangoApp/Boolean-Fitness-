from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('businesses/', views.business_index, name= 'index'),
    path('businesses/<int:business_id>/', views.business_detail, name= 'business_detail'),
    path('businesses/create/', views.BusinessCreate.as_view(), name= 'business_create'),
    path('groupclasses/', views.groupclass_index, name= 'class_index'),
    path('groupclasses/<int:groupclass_id>/', views.groupclass_detail, name= 'class_detail'),
    path('groupclasses/create', views.GroupClassCreate.as_view(), name= 'class_create'),
    path('wellnesscoaches/',views.coach_index, name='coach_index'),
    path('profile/', views.profile, name= 'profile'),
    path('accounts/signup/', views.signup, name='signup'),

]
