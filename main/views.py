from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from main.models import *
from RateMyLandlord import secrets
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.template.loader import render_to_string
import hashlib, datetime, random


def index(request):
    return render(request, 'main/index.html')

def search(request):
    form = SearchForm()
    return render(request, 'main/search.html', {'search_form' : form})

def register(request):
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Create User and save to db
            user = User(first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'],
                        is_active=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Generate activation key
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            act_key = hashlib.sha1((salt+form.cleaned_data['email']).encode('utf-8')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            user = User.objects.get(email=form.cleaned_data['email'])

            # Create account and save to db
            account = Account(user=user, activation_key=act_key,key_expires=key_expires,residence=None,school=get_school(user.email))
            account.save()

            # Send account confirmation email
            subject = 'RateMyLandlord Account Confirmation'
            url = ''.join(['https://',get_current_site(request).domain,'/accounts/confirm/'+act_key])
            body_text = render_to_string('email/text/confirmation.txt',{'user':user,'url':url})
            body_html = render_to_string('email/html/confirmation.html',{'user':user,'url':url})

            send_mail(subject,body_text,secrets.EMAIL_USER,[user.email],html_message=body_html,fail_silently=False)
            return render(request,'main/account_success.html',{})
        else:
            return render(request,'main/register.html',{'register_form': form})
    else:
        return render(request,'main/register.html',{'register_form': form})

def account_confirm(request, activation_key):
    if request.user.is_authenticated():
        return redirect('/')

    account = get_object_or_404(Account, activation_key=activation_key)

    if account.key_expires < timezone.now():
        account.delete()
        return render(request, 'main/account_confirm.html',{'expired': True})

    user = account.user
    user.is_active = True
    user.save()
    
    return render(request,'main/account_confirm.html',{'expired': False})

def get_school(email):
    domain = email.split('@')[1]
    return School.objects.get(domain=domain)

