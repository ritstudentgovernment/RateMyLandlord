from django.db import models
from django.contrib.auth.models import User

class Landlord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    properties = models.ManyToManyField('Property')

class Complex(models.Model):
    name = models.CharField(max_length=150)
    landlord = models.ForeignKey(Landlord)

class Property(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    furnished = models.BooleanField()
    rooms = models.PositiveSmallIntegerField()
    complx = models.ForeignKey(Complex)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    properties = models.ManyToManyField(Property)

class School(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    residence = models.ForeignKey(Property)
    school = models.ForeignKey(School)

class Review(models.Model):
    user = models.ForeignKey(Account)
    text = models.CharField(max_length=300)
    prop = models.ForeignKey(Property)
    landlord = models.ForeignKey(Landlord)
    lease_start = models.DateTimeField()
    lease_end = models.DateTimeField()
    price = models.PositiveIntegerField()
    utilities = models.PositiveIntegerField()
    accessible = models.BooleanField()
    clean = models.BooleanField()
    laundry = models.BooleanField()

class LandlordReview(models.Model):
    responsive = models.PositiveSmallIntegerField()
    communication = models.PositiveSmallIntegerField()
    recommend = models.PositiveSmallIntegerField()
    landlord = models.ForeignKey(Landlord)

class TagCounter(models.Model):
    prop = models.ForeignKey(Property)
    tag = models.ForeignKey(Tag)
    count = models.PositiveIntegerField(default=0)
