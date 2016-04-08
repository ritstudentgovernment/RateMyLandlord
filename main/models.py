from django.db import models

class Complex(models.Models):
    name = models.CharField(max_length=150)
    landlord = models.ForeignKey(Landlord)

class Property(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    complx = models.ForeignKey(Complex)

class Landlord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    properties = models.ManyToManyField(Property)

