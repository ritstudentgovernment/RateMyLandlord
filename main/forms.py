from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class':'form-control',
                                                           'type':'text',
                                                           'size':'100',
                                                           'placeholder' : 'Search by address or landlord name'}),
                             label='',
                             required=False)

    max_dist = forms.DecimalField(max_value = 9999.99,
                                  min_value= 0,
                                  widget=forms.TextInput(attrs={'class':'form-control',
                                                                'size':'6',
                                                                'maxlength':'6'}),
                                  label='Max Dist(mi) ',
                                  required=False)

    max_cost = forms.DecimalField(max_value = 9999.99,
                                  min_value= 0,
                                  widget=forms.TextInput(attrs={'class':'form-control',
                                                                'size':'6',
                                                                'maxlength':'6'}),
                                  label='Max $$$ ',
                                  required=False)