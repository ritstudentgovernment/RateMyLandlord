from django.test import TestCase
from main.forms import *
from main.models import *

class FormTests(TestCase):
    def test_registration(self):
        School(name='RIT',domain='rit.edu',latitude=43.0845,longitude=77.6764).save()
        
        # Test valid email
        form_data = {
                        'first_name': 'First',
                        'last_name': 'Last',
                        'email': 'test@rit.edu',
                        'password': 'thisisatest',
                        'password_confirm': 'thisisatest',
                    }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test non-edu email
        form_data = {
                        'first_name': 'First',
                        'last_name': 'Last',
                        'email': 'test@test.com',
                        'password': 'thisisatest',
                        'password_confirm': 'thisisatest',
                    }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test non-participent school email
        form_data = {
                        'first_name': 'First',
                        'last_name': 'Last',
                        'email': 'test@mit.edu',
                        'password': 'thisisatest',
                        'password_confirm': 'thisisatest',
                    }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_login(self):
        User(username='confirm@rit.edu',email='confirm@rit.edu',password='test',is_active=True).save()
        User(username='noconfirm@rit.edu',email='noconfirm@rit.edu',password='test',is_active=False).save()

        form_data = {'email': 'confirm@rit.edu','password': 'test'}

        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        form_data = {'email': 'noconfirm@rit.edu','password': 'test'}

        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

