from django.contrib import admin
from .models import Business, GroupClass, Coach, Review

# Register your models here.
admin.site.register(Business)
admin.site.register(GroupClass)
admin.site.register(Coach)
admin.site.register(Review)
