from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if not password_confirm:
            raise ValidationError('You must confirm your password!')
        if password != password_confirm:
            raise ValidationError('Passwords do not match!')

        return password_confirm

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

class LoginForm(forms.Form):
    email = forms.CharField(max_length=254,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(max_length=25,
                widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password'}),
                label='Password')
   
    def clean_email(self):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except:
            user = None
        if user:
            if user.is_active:
                return self.cleaned_data['email']
            else:
                raise ValidationError('You must first confirm your account!')
        else:
            raise ValidationError('Account does not exist')
        
