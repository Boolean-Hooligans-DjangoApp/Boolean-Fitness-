from django.contrib import admin
from .models import Business, GroupClass, Coach, Review, CoachReview, BusinessReview

# Register your models here.
admin.site.register(Business)
admin.site.register(GroupClass)
admin.site.register(Coach)
admin.site.register(Review)
admin.site.register(CoachReview)
admin.site.register(BusinessReview)
