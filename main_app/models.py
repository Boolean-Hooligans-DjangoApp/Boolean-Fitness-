from django.db import models
from django.urls import reverse
from datetime import date


REVIEWS = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

BUSINESS_TYPES = (
    ('Yoga', 'Yoga'),
    ('Gym', 'Gym'),
    ('Chiropractor','Chiropractor'),
    ('Resturant', 'Resturant'),
    ('Shop', 'Shop'),
    ('Acupuncture','Acupuncture'),
    ('Massage', 'Massage'),
    )

BUSINESS_HOURS = (
    ('24 hours a day', '24 hours a day'),
    ('Hours to be determined', 'Hours to be determined'),
    ('Contact business for more information', 'Contact business for more information'),
    ('8am - 5pm', '8am - 5pm'),
    ('8am - 10pm', '8am - 10pm'),
    ('6am - 10pm', '6am - 10pm'),
    ('12pm - 12am', '12pm - 12am'),
    ('9am - 6pm', '9am - 6pm'),
    ('Closed for the Holidays', 'Closed for the Holidays'),
)

class Business(models.Model):
    name = models.CharField(max_length=100, help_text='Please enter the name of your business / establishment')
    email = models.CharField(max_length=100, help_text='e.g. example@email.com')
    location = models.PositiveIntegerField('Zip Code',  help_text='Please enter your 5 digit zip or postal code')
    business_type = models.CharField(
        max_length=100,
        choices= BUSINESS_TYPES,
        default=BUSINESS_TYPES[0][0]
        )
    business_hours = models.CharField(
        max_length= 100,
        choices= BUSINESS_HOURS,
        default= BUSINESS_HOURS[0][0]
    )
    rates = models.TextField(max_length=500, help_text='Please add the rates and prices of the services / goods you offer')

    def __str__(self):
        return self.name, self.business_type

    def get_absolute_url(self):
        return reverse("business_detail", kwargs={"business_id": self.id})


class GroupClass(models.Model):
    name = models.CharField(max_length=100, help_text='Please enter the name of your group class / activity')
    date = models.DateField('Group Class Date', help_text='Please select the date the event will take place')
    description = models.TextField(max_length=500, help_text='Please add any additional information regarding the event')

    def __str__(self):
        return f"{self.description} on {self.date}"

    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"groupclass_id": self.id})


class Coach(models.Model):
    name = models.CharField(max_length=100, help_text='Please enter your name here')
    email = models.CharField(max_length=100, help_text='e.g. example@email.com')
    location = models.PositiveIntegerField('Zip Code', help_text='Please enter your 5 digit zip or postal code')
    specialty = models.CharField(max_length=100, help_text='Please enter your specialty / area of expertise here')
    bio = models.TextField(max_length=250, help_text='Please add additional information about your qualifications and program')
    availability = models.TextField(max_length=250, help_text='Please add information regarding your availability')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coach_detail", kwargs={"coach_id": self.id})


class Review(models.Model):
    # coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    # business = models.ForeignKey(Business, on_delete=models.CASCADE)
    groupclass = models.ForeignKey(
        GroupClass, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=1,
        choices=REVIEWS,
        default=REVIEWS[0][0]
    )
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(("Date"), default=date.today)

    def __str__(self):
        return f"{self.review} on {self.comment}"

class CoachReview(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=1,
        choices=REVIEWS,
        default=REVIEWS[0][0]
    )
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(("Date"), default=date.today)

    def __str__(self):
        return f"{self.review} on {self.comment}"

class BusinessReview(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=1,
        choices=REVIEWS,
        default=REVIEWS[0][0]
    )
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(("Date"), default=date.today)

    def __str__(self):
        return f"{self.review} on {self.comment}"

