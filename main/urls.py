from django.conf.urls import url
from . import  views

app_name='main'

urlpatterns= [
    url(r'^$', views.index, name='index'),
    #url(r'about', views.about, name='about'),
    url(r'search/', views.search, name='search'),
    url(r'search/(\w*)', views.search, name='search_query'),
    url(r'register/', views.register, name='register'),
    url(r'accounts/confirm/(?P<activation_key>\w+)/', views.account_confirm, name='account_confirm'),
    #url(r'property/(\w+)/(\w+)', views.property, name='property'),
    #url(r'landlord/(\w+)/(\w+)', views.landlord, name='landlord'),
]
