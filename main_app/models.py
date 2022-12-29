from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    business_hours = models.TextField(max_length=250)
    rates = models.TextField(max_length=250)