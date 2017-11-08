from django.conf.urls import url
from about.views import *

urlpatterns = [
    url(r'^about', about, name='about'),
    url(r'^contact', contact, name='contact'),
    url(r'^members', members, name='members'),
    url(r'^tangcard', tangcard, name='tangcard'),
]