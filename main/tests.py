from django.test import TestCase
from main.forms import RegistrationForm
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

        # Test not strong password
        form_data = {
                        'first_name': 'First',
                        'last_name': 'Last',
                        'email': 'weakpassword@rit.edu',
                        'password': '1',
                        'password_confirm': '1',
                    }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

