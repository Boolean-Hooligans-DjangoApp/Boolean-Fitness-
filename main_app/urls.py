from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('businesses/', views.business_index, name= 'index'),
    path('businesses/<int:business_id>/', views.business_detail, name= 'business_detail'),
    path('businesses/create/', views.BusinessCreate.as_view(), name= 'business_create'),
    path('businesses/<int:pk>/update/', views.BusinessUpdate.as_view(), name= 'business_update'),
    path('businesses/<int:pk>/delete/', views.BusinessDelete.as_view(), name= 'business_delete'),
    path('groupclasses/', views.groupclass_index, name= 'class_index'),
    path('groupclasses/<int:groupclass_id>/', views.groupclass_detail, name= 'class_detail'),
    path('groupclasses/create', views.GroupClassCreate.as_view(), name= 'class_create'),
    path('groupclasses/<int:pk>/update/', views.GroupClassUpdate.as_view(), name= 'class_update'),
    path('groupclasses/<int:pk>/delete/', views.GroupClassDelete.as_view(), name= 'class_delete'),
    path('coaches/',views.coach_index, name='coach_index'),
    path('coaches/<int:coach_id>/', views.coach_detail, name= 'coach_detail'),
    path('coaches/create', views.CoachCreate.as_view(), name= 'coach_create'),
    path('coaches/<int:pk>/update/', views.CoachUpdate.as_view(), name= 'coach_update'),
    path('coaches/<int:pk>/delete/', views.CoachDelete.as_view(), name= 'coach_delete'),
    path('profile/', views.profile, name= 'profile'),
    path('accounts/signup/', views.signup, name='signup'),

]
