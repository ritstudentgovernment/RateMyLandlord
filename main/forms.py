from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password 

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class':'form-control'}),
                             label='')
    max_dist = forms.IntegerField(max_value = 9999,
                                  min_value= 0,
                                  widget=forms.TextInput(attrs={'class':'form-control'}),
                                  label='Max Dist:')
    max_cost = forms.DecimalField(max_value = 9999.99,
                                  min_value= 0,
                                  widget=forms.TextInput(attrs={'class':'form-control'}),
                                  label='Max $$$:')

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
                                label='First Name')
    last_name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
                                label='Last Name')
    email = forms.EmailField(max_length=50,
            widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            label='Email'
            )
    password = forms.CharField(max_length=25,
                widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password'}),
                label='Password')
    password_confirm = forms.CharField(max_length=25,
                widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Confirm Password'}),
                label='Confirm Password')

    def clean(self):
        super(RegistrationForm, self).clean()
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        
        validate_password(password)
        
        if not password_confirm:
            raise ValidationError('You must confirm your password!')
        if password != password_confirm:
            raise ValidationError('Passwords do not match!')

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if len(User.objects.filter(email=email)) > 0:
            raise ValidationError('User already exists!')

        validate_email(email)
        
        # Check if email is a .edu
        if not email.endswith('.edu'):
            raise ValidationError('You must use a .edu email address to register!')

        schools = School.objects.all()

        # Set domains to be an array with all valid school domains
        domains = [school.domain for school in schools]
        
        # Check if email domain is from a participating school
        if email.endswith(tuple(domains)):
            return email
        else:
            raise ValidationError('Your school does not participate in RateMyLandlord')


