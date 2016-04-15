from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'main\index.html')

def search(request):
    form = SearchForm()
    return render(request, 'main\search.html', {'search_form' : form})
