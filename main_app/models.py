from django.db import models
from django.urls import reverse


REVIEWS = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

BUSINESS_TYPES = (
    ('Y', 'Yoga'),
    ('G', 'Gym'),
    ('C','Chiropractor'),
    ('R', 'Resturant'),
    ('S', 'Shop'),
    ('A','Acupuncture'),
    ('M', 'Massage'),
    )

BUSINESS_HOURS = (
    ('1', '24 hours a day'),
    ('2', 'Hours to be determined'),
    ('3', 'Contact business for more information'),
    ('4', '8am - 5pm'),
    ('5', '8am - 10pm'),
    ('6', '6am - 10pm'),
    ('7', '12pm - 12am'),
    ('8', '9am - 6pm'),
    ('9', 'Closed for the Holidays'),
)

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    business_type = models.CharField(
        max_length=1,
        choices= BUSINESS_TYPES,
        default=BUSINESS_TYPES[0][0]
        )
    business_hours = models.CharField(
        max_length= 1,
        choices= BUSINESS_HOURS,
        default= BUSINESS_HOURS[0][0]
    )
    rates = models.TextField(max_length=250)

    def __str__(self):
        return self.name, self.business_type

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
    specialty = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    availability = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coach_detail", kwargs={"coach_id": self.id})


class Review(models.Model):
    groupclass = models.ForeignKey(
        GroupClass, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=1,
        choices=REVIEWS,
        default=REVIEWS[0][0]
    )
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.review} on {self.comment}"
