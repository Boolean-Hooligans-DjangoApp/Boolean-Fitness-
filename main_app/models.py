from django.db import models
from django.urls import reverse

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    business_hours = models.TextField(max_length=250)
    rates = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("business_detail", kwargs={"business_id": self.id})

class GroupClass(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Group Class Date')
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.description} on {self.date}"
    
    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"groupclass_id": self.id})

class Coach(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    coach_specialty = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    availability = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("business_detail", kwargs={"business_id": self.id})