from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request, 'main\index.html')

def search(request):
    if request.method == 'GET' and len(request.GET) > 0:
        form = SearchForm(request.GET)
        if(form.is_valid()):
            search = form.cleaned_data['search'].lower()
            maxdist = form.cleaned_data['max_dist']
            maxcost = form.cleaned_data['max_cost']
            properties = Property.objects.filter(address__istartswith=search)

            return render(request, 'main/search.html', {'properties': properties, 'search_form': form})
        else:
            return render(request, 'main/search.html', {'search_form' : form})
    else:
        form = SearchForm()

        return render(request, 'main\search.html', {'search_form' : form})

