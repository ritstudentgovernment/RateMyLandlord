from django import forms

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